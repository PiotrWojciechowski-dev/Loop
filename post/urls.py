from django.urls import path
from .views import HomeView
from .views import get_post



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('makepost.urls', get_post.as_view(), name='makepost'),
]