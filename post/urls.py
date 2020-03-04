from django.urls import path
from .views import HomeView, PostDeleteView, PostUpdateView




urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<pk>/edit/', PostUpdateView.as_view(), name = 'change_post'),
    path('<pk>/delete/', PostDeleteView.as_view(), name= 'delete_post'),
]