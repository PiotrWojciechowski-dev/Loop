from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('created/', views.profile_created, name='created_profile'),
    path('', views.profile_detail, name='profile_detail'),
]