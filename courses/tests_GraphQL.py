import json

from graphene_django.utils.testing import GraphQLTestCase
from coursespro.schema import schema
from .models import Course, Lesson


class GraphQLTests (GraphQLTestCase):

    GRAPHQL_SCHEMA = schema
    GRAPHQL_URL = '/graphql/'


    def test_all_courses(self):
        response = self.query(
            '''
        query {
          allCourses {
            title
            description
          }
        }
            '''
            #op_name='all_courses'
        )
        self.assertResponseNoErrors(response)


    def test_all_lessons(self):
        response = self.query(
            '''
        query {
          allLessons {
            title
            description
          }
        }
            '''
        )
        self.assertResponseNoErrors(response)


    def test_all_teachers(self):
        response = self.query(
            '''
        query {
          allTeachers {
            user {
              id,
              username
            }
          }
        }
            '''
        )
        self.assertResponseNoErrors(response)

    def test_one_lesson(self):
        c = Course.objects.create(title="test course title")
        l = Lesson.objects.create(title="test lesson title", course=c)
        response = self.query(
            '''
        query {
          oneLesson (id: 1) {
            title,
            description,
            course {
              id,
              title
            }
          }
        }
            '''
        )
        self.assertResponseNoErrors(response)

    def test_mutation(self):
        c = Course.objects.create(title="test course title")
        l = Lesson.objects.create(title="test lesson title", course=c)
        response = self.query(
            '''
mutation {
  changeLesson (title: "New GraphQL title", description: "New GRaphQL is cool Description", id: 1) {
    lesson {
      title
      description
    }
  }
}
            '''
        )
        self.assertResponseNoErrors(response)