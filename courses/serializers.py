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


class CourseCreateSerializer(serializers.ModelSerializer):

    lessons = LessonSerializer(many=True, required=False)
    teacher = TeacherSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons', 'teacher')



    def create(self, validated_data):
        lessons = validated_data.pop('lessons', [])
        instance = Course.objects.create(**validated_data)
        #Lesson.objects.create(Course=instance)
        for lessons_data in lessons:
            lesson= Lesson.objects.get(pk=lessons_data.get('id'))
            instance.tasks.add(lesson)
        return instance

    def update(self, instance, validated_data):
        lessons = validated_data.pop('lessons', [])
        instance = super().update(instance, validated_data)
        for lessons_data in lessons:
            lesson = Lesson.objects.get(pk=lessons_data.get('id'))
            instance.tasks.add(lesson)
        return instance