from django.urls import path
from .views import HomeView
from .views import PostListView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path(
        'post-list/',
        PostListView.as_view(),
        name='posts-list'
    ),

]