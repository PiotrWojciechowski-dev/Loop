from django.urls import path
from .views import (   
    ProfileListView,
    ProfileCreateView,
    ProfileDetailView,
    ProfileUpdateView,
    ProfileDeleteView
    )

app_name = 'profiles'
urlpatterns = [
        path(
            '',
            ProfileListView.as_view(),
            name='profiles-list'
        ),
        path(
            'create/',
            ProfileCreateView.as_view(),
            name='profiles-create'
        ),
        path(
            '<int:id>/detail/',
            ProfileDetailView.as_view(),
            name='profiles-detail'
        ),
        path(
            '<int:id>/delete/',
            ProfileDeleteView.as_view(),
            name='profiles-delete'
        ),
        path(
            '<int:id>/update/',
            ProfileUpdateView.as_view(),
            name='profiles-update'
        ),
]