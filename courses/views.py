from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Course, Lesson
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import CourseSerializer, LessonSerializer



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

class CoursesDetailView(APIView):


    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        data = CourseSerializer(course).data
        return Response(data)

class LessonView (APIView):

    # def get(self, request):
    #     lesson = Lesson.objects.all().select_related('course')
    #     serializer = LessonSerializer(lesson, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        data = LessonSerializer(lesson).data
        return Response(data)
