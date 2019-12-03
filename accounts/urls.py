from django.urls import path
from .views import UserCreate, LoginView, LogoutView, ProfileView
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register', UserCreate.as_view(), name='user_create'),
    path('login/', views.LoginView.as_view(), name='login'),
    path("api-token-auth/", obtain_auth_token, name="obtain"),
    path ('logout/', views.LogoutView.as_view(), name ='logout'),
    path ('profile/', views.ProfileView.as_view(), name = 'profile'),
    #path ('profile/update', views.ProfileUpdateView.as_view(), name = 'profile_update'),


]

#or to add it into the main url files
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)