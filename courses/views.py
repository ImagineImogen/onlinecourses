from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from .models import Course, Lesson
from accounts.models import Student, Teacher
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import CourseSerializer, LessonSerializer, CourseCreateSerializer
from accounts.permissions import IsAdminUserOrAuthenticatedOrReadOnly
from rest_framework import generics
from .tasks import send_email_task
from .forms import QuestionForm






class CoursesListView(APIView):

    #permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        #courses = Course.objects.prefetch_related('teacher').all()
        courses = Course.objects.prefetch_related(Prefetch('teacher', queryset=Teacher.objects.select_related('user').all())).all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CoursesDetailView(APIView):

    permission_classes = (IsAdminUserOrAuthenticatedOrReadOnly,)

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        data = CourseSerializer(course).data
        return Response(data)


    def post(self, request, pk):
        user = request.user
        course = get_object_or_404(Course, pk=pk)

        if user not in course.student.all():
            user.is_student = True
            user.save()
            student, created = Student.objects.get_or_create(user=user)
            course.student.add(student)
            message = {"Сongratulations! You have successfully signed up for the course"}
            return Response(message, status=status.HTTP_201_CREATED)
        else:
            message = {"Looks like you've already been enrolled."}
            return Response(message, status=status.HTTP_304_NOT_MODIFIED)


class CourseDetailDeleteView (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUserOrAuthenticatedOrReadOnly,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def update(self, request, *args, **kwargs):
        serializer = CourseSerializer(instance=self.get_object(), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class CourseCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer

class LessonView (APIView):

    # def get(self, request):
    #     lesson = Lesson.objects.all().select_related('course')
    #     serializer = LessonSerializer(lesson, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk):
        lesson = get_object_or_404(Lesson.objects.select_related('course'), pk=pk)
        data = LessonSerializer(lesson).data
        return Response(data)


class AboutUsView (APIView):

    def post (self, request):
        form_data = request.data
        form = QuestionForm(form_data)
        
        if form.is_valid():
            task_data = form.cleaned_data
            send_email_task.delay(**task_data)
            message = {"Thank you! Your question has been submitted"}
            return Response (message, status=status.HTTP_202_ACCEPTED)
        else:
            message = {"Your question or email is not valid. Please try again later"}
            return Response (message, status=status.HTTP_400_BAD_REQUEST)

