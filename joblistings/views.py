# views.py
import numpy as np
from django.shortcuts import render
from .models import *  # Import your Job model
from django.db.models import Q


def home(request):
    return render(request, 'home.html')

def job_list(request):
    jobs = Job.objects.all()  # Retrieve job listings from MongoDB
    return render(request, 'job-list.html', {'jobs': jobs})
    # You can pass other context data as needed



def search_jobs(request):
    jobs = Job.objects.all()
    query = request.GET.get('query')  # Get the 'query' parameter from the request
    if query:  # Check if query is not None or empty
        jobs = Job.objects.filter(location__icontains=query)  # Use the query in the filter
        # ... rest of your view logic handling 'jobs'

    return render(request, 'job-list.html', {'jobs': jobs})





#numpy
def calculate_average_salary():
    jobs = Job.objects.filter(job_title='python_developer', city='Bangalore')

    salaries = [job.salary for job in jobs]
    
    if len(salaries) > 0:
        average_salary = np.mean(salaries)
        return average_salary
    else:
        return None 
    
    
    