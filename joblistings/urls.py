# urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('', views.job_list, name='job_list'),  # Job listings page
    # Add other URLs as needed for search, edit, delete functionalities
    path('search/', views.search_jobs, name='search'),
]
