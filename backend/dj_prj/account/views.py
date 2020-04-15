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


class LoginView(APIView):
    '''
    
    Login view.

    '''

    permission_classes = (AllowAny,)
    serializer_class = LoginRequestSerializer
    def post(self, request, format=None):
        return Response(LoginResponseSerializer({'status': 0, 'message': 'ok'}).data)
