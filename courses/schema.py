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
        fields = ('id', 'title', 'description', 'course')
'''
Course Field is a Foreign key
All query-able related models must be defined as DjangoObjectType subclass, or they will fail to show if you are trying to query those relation fields. You only need to create the most basic class for this to work. 
'''

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
    all_lessons = graphene.List(LessonType)
    one_lesson = graphene.Field(LessonType, id = graphene.Int())

    def resolve_all_courses(self, info, **kwargs):
        return Course.objects.prefetch_related('teacher').all()

    def resolve_all_teachers(self, info, **kwargs):
        return Teacher.objects.all()

    def resolve_all_lessons(self, info, **kwargs):
        return Lesson.objects.select_related('course').all()

    def resolve_one_lesson(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Lesson.objects.get(pk=id)

        return None


class ChangeLesson(graphene.Mutation):

    class Arguments:
        #input
        title = graphene.String()
        description = graphene.String(required=False)
        id = graphene.ID()

    # The class attributes define the response of the mutation
    lesson = graphene.Field(LessonType)

    def mutate(self, info, title, id, description ):
        _lesson = Lesson.objects.get(pk=id)
        _lesson.title = title
        _lesson.description = description
        _lesson.save()

        if not _lesson:
            raise graphene.GraphQLerror
        return ChangeLesson (lesson=_lesson)


class Mutation:
    change_lesson = ChangeLesson.Field()