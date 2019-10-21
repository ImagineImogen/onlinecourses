from django.urls import path
from .views import UserCreate, LoginView, LogoutView
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', UserCreate.as_view(), name='user_create'),
    path('login/', views.LoginView.as_view(), name='login'),
    path("api-token-auth/", obtain_auth_token, name="obtain"),
    path ('logout/', views.LogoutView.as_view(), name ='logout'),

]