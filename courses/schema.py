from graphene_django import DjangoObjectType
import graphene
from .models import Course, Lesson
from accounts.models import Teacher, Student, MyUser

class CourseType(DjangoObjectType):
    class Meta:
        model = Course


class LessonType(DjangoObjectType):
    class Meta:
        model = Lesson


class UserType(DjangoObjectType):
    class Meta:
        model = MyUser


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query(object):
    all_courses = graphene.List(CourseType)
    all_teachers = graphene.List(TeacherType)

    def resolve_all_courses(self, info, **kwargs):
        return Course.objects.prefetch_related('teacher').all()

    def resolve_all_teachers(self, info, **kwargs):
        return Teacher.objects.all()