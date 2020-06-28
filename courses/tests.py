from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from accounts.models import MyUser




class TokenAuth (APITestCase):

    def test_api_token(self):
        u = MyUser.objects.create_user(username='testuser', email='testuser@example.com', password='testuser')
        u.is_active = True
        u.save()
        resp = self.client.post('/users/login/', {'username': 'testuser', 'password': 'testuser'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in resp.data)

# Create your tests here.
