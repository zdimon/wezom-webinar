from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from rest_framework.authtoken.models import Token


from account.models import UserProfile

def create_user(login,password):
    user = UserProfile()
    user.username = login
    user.set_password(password)
    user.save()
    token = Token.objects.create(user=user)
    return token



class AuthenticationTest(APITestCase):

    def test_user_can_not_login(self):
        response = self.client.post(reverse('user-login'),data={
            'username': 'admin',
            'password': 'admin'
        })

        self.assertEqual(response.data['status'], 1)

    def test_user_can_login_by_username_and_password(self):

        token = create_user('admin','123')

        response = self.client.post(reverse('user-login'),data={
            'username': 'admin',
            'password': '123'
        })

        self.assertEqual(response.data['status'], 0)

        response_fail = self.client.post(reverse('user-login'),data={
            'username': 'admin',
            'password': 'blabla'
        })

        self.assertEqual(response_fail.data['status'], 1)

        try:
            token_str = response.data['token']
        except:
            self.fail('No token in the response!')

        self.assertEqual(response.data['token'],token.key)