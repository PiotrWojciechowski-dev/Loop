from django.urls import path
from . import views

app_name = 'groupchat'
urlpatterns = [
    path('<str:recipient>/<str:sender>', views.GroupMessageView.as_view(), name='messaging'),
]