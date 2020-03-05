from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('detail/<str:username>', views.ProfileView.as_view(), name='profile_detail'),
    path('<int:pk>/update/', views.ProfileUpdateView.as_view(), name='update_profile'),
]