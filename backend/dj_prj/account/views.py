from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
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


