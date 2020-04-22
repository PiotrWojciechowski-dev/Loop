from django.urls import path
from . import views

app_name = 'groupchat'
urlpatterns = [
    path('<int:groupchat_id>/<str:groupchat_name>', views.GroupMessageView.as_view(), name='messaging'),
]