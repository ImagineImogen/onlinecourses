from django.shortcuts import render, get_object_or_404
from .serializers import UserSerializer, LoginSerializer, LogoutSerializer,ProfileSerializer, AddProfileSerializer
from rest_framework import generics, status, permissions
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import pysnooper
from .models import Profile



class UserCreate(generics.CreateAPIView):
    model = get_user_model()
    authentication_classes = ()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer



class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def get(self, request):
        user = request.user
        if not user or not user.id:
            return Response({'msg': 'You are not logged in'})
        return Response({'msg': f'You are already logged in as {user}'})


    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)

        if user.is_active:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            instance, created = Profile.objects.get_or_create(user=request.user)
            instance.save()
            return Response({'token': token.key}, status=200)

        return Response({'error': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    serializer_class = LogoutSerializer

    # authentication_classes = (TokenAuthentication,)
    def get(self, request):

        user = request.user
        if not user or not user.id:
            return Response({'msg': 'you are not logged in'})
        return Response({'msg': f'you are logged in as {user}'})


    def post (self, request):
        #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        logout(request)
        return Response('Logout successful', status=204)


class ProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)


    def get(self, request):

        profile = request.user.profile

        serializer = ProfileSerializer(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request):
        profile = request.user.profile
        user = request.user
        data = request.data
        serializer_user = UserSerializer(user, data=data, partial=True)
        serializer = ProfileSerializer(profile, data=data, partial=True)
        # if serializer_user.is_valid():
        #     serializer_user.save()
        if serializer.is_valid() and serializer_user.is_valid():
            serializer.save()
            serializer_user.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileUpdateView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        profile = request.user.profile

        serializer = ProfileSerializer(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        profile = request.user.profile
        user = request.user
        data = request.data
        serializer = AddProfileSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

