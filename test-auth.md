## Create a new tests dir in account app.

    mkdir account/tests


    # test_auth.py


    from rest_framework import status
    from rest_framework.reverse import reverse
    from rest_framework.test import APITestCase

    class AuthenticationTest(APITestCase):

        def test_user_can_login(self):
            response = self.client.post(reverse('user-login'),data={
                'username': 'admin',
                'password': 'admin'
            })
            print(response.status_code)

## Run test

    ./manage.py test account.tests

    django.urls.exceptions.NoReverseMatch: Reverse for 'user-login' not found. 'user-login' is not a valid view function or pattern name.

    ----------------------------------------------------------------------
    Ran 1 test in 0.004s

    FAILED (errors=1)
    Destroying test database for alias 'default'...


## Create a new view.


    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework.permissions import IsAuthenticated, AllowAny

    from rest_framework import serializers

    class LoginRequestSerializer(serializers.Serializer):
        login = serializers.CharField()
        password = serializers.CharField()

    class LoginResponseSerializer(serializers.Serializer):
        status = serializers.IntegerField()
        message = serializers.CharField()  

    class LoginView(APIView):
        '''
        
        Login view.

        '''

        permission_classes = (AllowAny,)
        serializer_class = LoginRequestSerializer

        def post(self, request, format=None):
            return Response(LoginResponseSerializer({'status': 0, 'message': 'ok'}).data)



## Define the routing.

    # dj_prj/urls.py

    urlpatterns = [
        ...
        path('user/login',LoginView.as_view(),name="user-login"),
        ...

## Compleate test


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


## Compleate view


    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework.permissions import IsAuthenticated, AllowAny

    from rest_framework import serializers
    from rest_framework.authtoken.models import Token


    class LoginRequestSerializer(serializers.Serializer):
        login = serializers.CharField()
        password = serializers.CharField()

    class LoginResponseSerializer(serializers.Serializer):
        status = serializers.IntegerField()
        message = serializers.CharField()  
        token = serializers.CharField()

    from account.models import UserProfile

    class LoginView(APIView):
        '''
        
        Login view.

        '''

        permission_classes = (AllowAny,)
        serializer_class = LoginRequestSerializer
        @swagger_auto_schema( 
            operation_description="Login user by username and password.", \
            request_body=LoginRequestSerializer, \
            responses={200: LoginResponseSerializer} )
        def post(self, request, format=None):
            username = request.data['username']
            password = request.data['password']

            try:
                user = UserProfile.objects.get(username=username)
                token, created = Token.objects.get_or_create(user=user)
                if user.check_password(password):
                    res = {'status': 0, 'message': 'Welcome %s' % user.username, 'token': token.key}
                else: 
                    res = {'status': 1, 'message': 'Password is incorrect!', 'token': None}

            except Exception as e:
                res = {'status': 1, 'message': str(e), 'token': 'None'}
                
            return Response(LoginResponseSerializer(res).data)






