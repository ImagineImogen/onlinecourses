from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from accounts.models import MyUser
from .models import Course
from .views import *
from rest_framework import status
from rest_framework.test import APIClient



class TokenAuth (APITestCase):

    def test_api_token(self):
        u = MyUser.objects.create_user(username='testuser', email='testuser@example.com', password='testuser')
        u.is_active = True
        u.save()
        resp = self.client.post('/users/login/', {'username': 'testuser', 'password': 'testuser'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)


class TestCoursesListView(APITestCase):


    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CoursesListView.as_view()
        self.uri = '/api/'

    def test_get(self):
        request = self.factory.get(self.uri)
        #response = self.client.get(self.uri)

        response = self.view(request)
        self.assertEqual(response.status_code, 200,
        'Expected Response Code 200, received {0} instead.'
        .format(response.status_code))


class TestCoursesDetailView(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CoursesDetailView.as_view()
        self.uri = '/api/'

    def test_get(self):
        client = APIClient()
        u = Course.objects.create(title="test title")
        response = client.get(self.uri, pk=u.id, format='api')

        # request = self.factory.get(self.uri)
        # response = self.view(request, pk=u.id)

        self.assertEqual(response.status_code, 200,
        'Expected Response Code 200, received {0} instead.'
        .format(response.status_code))
        self.assertContains(response, 'title')

    # def test_post(self):
    #     request = self.factory.get(self.uri)
    #     response = self.view(request)
    #     self.assertEqual(response.status_code, 304,
    #     'Expected Response Code 304, received {0} instead.'
    #     .format(response.status_code))