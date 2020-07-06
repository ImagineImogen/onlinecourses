from django.test import TestCase
from rest_framework.test import APITestCase, APISimpleTestCaseб
from rest_framework.test import APIRequestFactory
from accounts.models import MyUser
from accounts.views import *
from .models import Course
from .views import *
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model



class TokenAuth (APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.request_factory = APIRequestFactory()
        u = MyUser.objects.create_user(username='testuser', email='testuser@example.com', password='testuser')
        u.is_active = True
        u.save()

    def test_api_token(self):
        resp = self.client.post('/users/login/', {'username': 'testuser', 'password': 'testuser'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)

class SimpleTest (APISimpleTestCase):

    def simple_test(self):
        u= MyUser.objects.create_user(username='testuser', email='testuser@example.com', password='testuser')

        self.assertEqual(u.username,'testuser')

class TestCoursesListView(APITestCase):


    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CoursesListView.as_view()
        self.uri = '/api/'

    def test_get(self):
        request = self.factory.get(self.uri)
        response = self.client.get(self.uri)

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

class TestCourseDetailDeleteView(APITestCase):
    def setUp(self):
        self.uri = '/api/1'
        self.data = {
                "title": "new test title",
                "description": "test"}
        self.course = Course.objects.create(title="test title")
        self.client = APIClient()


    def test_update_without_credentials(self):
        response = self.client.post(
            self.uri,
            self.data,)
        self.assertEqual(response.status_code, 401,
        'Expected Response Code 401, received {0} instead.'
        .format(response.status_code))


    def update_with_appropriate_credentials(self):
        #admin = setup_admin()
        myuser = get_user_model().objects.create_superuser(
                "admintest",
                "admintest@admintest.com",
                "admintest"
            )
        #self.client.login(username='admintest', password='admintest')
        self.client.force_authenticate(user=myuser)
        response = self.client.post(
            self.uri,
            data = {
                "title": "new test title",
                "description": "test"
            },)

        self.assertEqual(response.status_code, 200,
        'Expected Response Code 200, received {0} instead.'
        .format(response.status_code))

class TestLessonView(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(TestLessonView, cls).setUpClass()
        course_test = Course.objects.create(title="Test")
        lesson_test = Lesson.objects.create(title="Test", course=course_test)


    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = LessonView.as_view()
        self.uri = '/api/lessons/'

    def test_get(self):
        c = APIClient()
        # course_test = Course.objects.create(title="test title")
        # lesson_test = Lesson.objects.create(title="new test lesson", course=course_test)
        request = self.factory.get(self.uri)
        response = self.view(request, pk=1)
        self.assertEqual(response.status_code, 200)

class TestLoginView(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = LoginView.as_view()
        self.uri = '/users/login/'
        self.username = 'user'
        self.password = 'test123'

    def test_get(self):
        request = self.factory.get(self.uri)
        response = self.view(request)

        self.assertEqual(response.status_code, 200,
        'Expected Response Code 200, received {0} instead.'
        .format(response.status_code))
    def test_post(self):
        pass
        #tested in func test_api_token

class TestProfileView(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ProfileView.as_view()
        self.uri = '/users/profile/'
        self.username = 'user'
        self.password = 'test123',
        self.email = "test@example.com"

    def get_profile(self):
        myuser = get_user_model().objects.create_user(username=self.username,
            email = self.email,
            password=self.password
        )
        self.client.force_authenticate(user=myuser)
        request = self.factory.get(self.uri)

        response = self.view(request)

        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        self.assertTrue('bio' in response.data)


class TestUserCreate(APITestCase):


    def test_post(self):
        response = self.client.post('/users/register', data={'username': 'userexample', 'password': 'password', 'email': 'user@gmail.com'}, format='json')
        self.assertEqual(response.status_code, 201,
        'Expected Response Code 201, received {0} instead.'
        .format(response.status_code))