from django.urls import path
from post.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]