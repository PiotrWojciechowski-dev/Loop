from django.urls import path
from . import views

app_name = 'messages'
urlpatterns = [
    path('<str:recipient>/<str:sender>', views.MessageView.as_view(), name='messaging'),
]