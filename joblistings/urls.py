# urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('', views.job_list, name='job_list'),  # Job listings page
    # Add other URLs as needed for search, edit, delete functionalities
    path('search/', views.search_jobs, name='search'),
    
    path('jobs/<int:job_id>/edit/', views.edit_job, name='edit-job'),
    path('jobs/<int:job_id>/delete/', views.delete_job, name='delete-job'),
    
    
    #numpy
    path('average-salary/', views.job_list_view, name='job-list'),
]
