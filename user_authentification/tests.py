from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


## i'll create testcases for :
# 1- Test for Successful Login
# 2- Test for Login Failure with Invalid Credentials
# 3- Test for Successful Logout
# 4- Test for Logout Failure without Authentication
# 5- Refresh Token Test Case


class AuthenticationTests(APITestCase):
    def setUp(self):
        User = get_user_model()  
        self.user = User.objects.create_user(
            username='testuser', 
            email='testuser@example.com', 
            password='testpass123'
        )
        self.token_url = reverse('token_obtain_pair')  
        self.logout_url = reverse('logout') 
    
    def test_login_success(self):
        response = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('user_info', response.data)
        self.assertEqual(response.data['user_info']['username'], 'testuser')
        self.assertEqual(response.data['user_info']['email'], 'testuser@example.com')

    def test_login_failure_invalid_credentials(self):
        response = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'No active account found with the given credentials')

        
    def test_logout_success(self):
        # First, log in to get the access token
        login_response = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        access_token = login_response.data['access']  # Get the access token

        # Set the access token in the Authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        
        # Now attempt to log out
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)


    def test_logout_failure_without_token(self):
            response = self.client.post(self.logout_url)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
            self.assertIn('detail', response.data)


    def test_refresh_token_success(self):
        login_response = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        refresh_token = login_response.data['refresh']

        response = self.client.post(reverse('token_refresh'), {
            'refresh': refresh_token
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

