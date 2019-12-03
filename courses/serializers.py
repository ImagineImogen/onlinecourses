from rest_framework import serializers
from .models import Lesson, Course, Teacher



class LessonSerializer(serializers.ModelSerializer):

    course = serializers.StringRelatedField()  # to display the name instead of PK - available for GET requests only

    class Meta:
        model = Lesson

        fields = ('id', 'title', 'description', 'course')

class TeacherSerializer(serializers.ModelSerializer):


    teacher_name = serializers.CharField(source='user.username',
                                         read_only=True)


    class Meta:
        model = Teacher
        fields = ('teacher_name',)



class CourseSerializer (serializers.ModelSerializer):

    lessons = LessonSerializer(many=True)
    teacher = TeacherSerializer(many=True)


    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons', 'teacher')  #to separate serializer with students for teachers later

