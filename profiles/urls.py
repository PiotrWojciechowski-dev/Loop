from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('detail/', views.ProfileView.as_view(), name='profile_detail'),
]