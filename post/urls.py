from django.urls import path
from .views import HomeView, PostDeleteView, PostUpdateView, CommentDeleteView, CommentUpdateView
from post import views




urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<pk>/edit/', PostUpdateView.as_view(), name = 'change_post'),
    path('<pk>/delete/', PostDeleteView.as_view(), name= 'delete_post'),
    path('<pk>/edit_comment/', CommentUpdateView.as_view(), name = 'change_comment'),
    path('<pk>/delete_comment/', CommentDeleteView.as_view(), name= 'delete_comment'),
    path('<pk>/report_post/', views.report_post, name= 'report_post'),
    path('report_list/', views.get_report, name= 'report_list'),
    path('<int:pk>/ignore/', views.ignore_report, name= 'ignore_report'),
]