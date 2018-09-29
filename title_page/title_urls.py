from django.urls import path

from title_page import title_views

urlpatterns = [
    path('', title_views.AboutMeView.as_view(), name='me-view'),
    path('about/', title_views.AboutProject.as_view(), name='project-view'),
]
