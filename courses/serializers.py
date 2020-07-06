from rest_framework import serializers
from .models import Lesson, Course
from accounts.models import Teacher
import pysnooper



class LessonSerializer(serializers.ModelSerializer):

    course = serializers.StringRelatedField()  # to display the name instead of PK - available for GET requests only

    class Meta:
        model = Lesson

        fields = ('id', 'title', 'description', 'course')

class TeacherSerializer(serializers.ModelSerializer):


    teacher_name = serializers.CharField(source='user.username')


    class Meta:
        model = Teacher
        fields = ('teacher_name',)



class CourseSerializer (serializers.ModelSerializer):

    lessons = LessonSerializer(many=True, required=False)
    teacher = TeacherSerializer(many=True, required=False)


    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons', 'teacher')  #to separate serializer with students for teachers later

    @pysnooper.snoop('/home/lisa/otus/update.log')
    def update(self, instance, validated_data):
        lessons = validated_data.pop('lessons', [])
        teacher = validated_data.pop('teacher', [])
        instance = super().update(instance, validated_data)
        #print(instance.teacher)
        if teacher:
            teacher_count = instance.teacher.count()
            for teachers_data in teacher:
                teacher_from_json = teachers_data.get('user')['username']
                if teacher_count == 1:
                    teacherm2m = instance.teacher.first()
                    if not teacherm2m.user.username == teacher_from_json:
                        try:
                            instance.teacher.remove(teacherm2m)
                            new_teacher = Teacher.objects.get(user__username=teacher_from_json)
                            instance.teacher.add(new_teacher)
                        except Teacher.DoesNotExist:
                            continue
                elif teacher_count > 1:
                    teacher_list = instance.teacher.all().values_list('user__username', flat=True)
                    if teacher_from_json in teacher_list:
                        continue
                    else:
                        new_teacher = Teacher.objects.get(user__username=teacher_from_json)
                        instance.teacher.add(new_teacher)
        for lesson in lessons:
            lesson, updated = Lesson.objects.update_or_create( defaults={'description': lesson["description"]},  title= lesson["title"])
            instance.save()

        return instance


class CourseCreateSerializer(serializers.ModelSerializer):

    lessons = LessonSerializer(many=True, required=False)
    teacher = TeacherSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'lessons', 'teacher')


    def create(self, validated_data): #by default nested serializers are read-only
        lessons = validated_data.pop('lessons', [])
        teacher = validated_data.pop('teacher', [])
        instance = Course.objects.create(title=validated_data['title'], description=validated_data['description'])
        for lessons_data in lessons:
            Lesson.objects.create(course=instance, **lessons_data)
        for teachers_data in teacher:
            try:
                teacher_instance = Teacher.objects.get(user__username=teachers_data.get('user')['username'])
                instance.teacher.add(teacher_instance)
            except Teacher.DoesNotExist:
                continue #teacher will not be assigned
        return instance

