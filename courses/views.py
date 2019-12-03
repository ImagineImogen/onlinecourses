from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Course, Lesson
from accounts.models import Student
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import CourseSerializer, LessonSerializer
import pysnooper



# class CourseList(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     # def perform_create(self, serializer):
#     #     serializer.save(teacher=self.request.user)

class CoursesListView(APIView):

    #permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@pysnooper.snoop('/home/lisa/otus/enrollment.log')
class CoursesDetailView(APIView):


    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        data = CourseSerializer(course).data
        return Response(data)

    @pysnooper.snoop('/home/lisa/otus/enrollment.log')
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

class LessonView (APIView):

    # def get(self, request):
    #     lesson = Lesson.objects.all().select_related('course')
    #     serializer = LessonSerializer(lesson, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        data = LessonSerializer(lesson).data
        return Response(data)

# @pysnooper.snoop('/home/lisa/otus/enrollment.log')
# class EnrollmentOnCourseView(APIView):
#
#     permission_classes = (permissions.IsAuthenticated,)
#
    # def post(self, request):
    #     user = request.user
    #     pk = request.data.get('pk')
    #     course = get_object_or_404(Course, pk=pk)
    #
    #     if user not in course.student.all():
    #         course.student.add(user)
    #         message = {"Сongratulations! You have successfully signed up for the course"}
    #         return Response(message, status=status.HTTP_201_CREATED)
    #     else:
    #         message = {"Looks like you've already been enrolled."}
    #         return Response(message, status=status.HTTP_304_NOT_MODIFIED)