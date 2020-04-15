from django.shortcuts import render

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

from drf_yasg.utils import swagger_auto_schema

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
        return Response(LoginResponseSerializer({'status': 0, 'message': 'ok'}).data)
