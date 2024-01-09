# views.py
import numpy as np
from django.shortcuts import render
from .models import *  # Import your Job model
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect

from django.http import HttpResponse
# from django.db.models import Avg
# import re

def job_list(request):
    jobs = Job.objects.all()  # Retrieve job listings from MongoDB
    return render(request, 'job-list.html', {'jobs': jobs})




def search_jobs(request):
    jobs = Job.objects.all()
    query = request.GET.get('query')  
    if query:  # Check if query is not None or empty
        jobs = Job.objects.filter(location__icontains=query)  # Use the query in the filter
        

    return render(request, 'job-list.html', {'jobs': jobs})


def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    print(job)
    if request.method == 'POST':
        job.jobtitle = request.POST.get('job_title')
        job.company = request.POST.get('job_company')
        job.location = request.POST.get('job_location')
        job.summary = request.POST.get('job_summary')
        job.salary = request.POST.get('job_salary')
        job.save()
        return redirect('job_list')  # Redirect to job list after editing
    return render(request, 'edit_job.html', {'job': job})

def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    print(job)# Redirect to job list after deletion
    return render(request, 'confirm_delete.html', {'job': job})



    
    


  


#numpy
def job_list_view(request):
    jobs = Job.objects.filter(jobtitle='python_developer', location='Bangalore, Karnataka')
    #print("Number of jobs found:", len(jobs))

    avg_salary = Job.objects.get(company='BigWelt Infotech Pvt Ltd').salary
    
    salaries=[]
    for job in jobs:
        if job:
            salaries.append(job.salary)
    #print("Number of valid salaries found:", len(salaries))
    
    if salaries:
        average_salary = np.mean(salaries)
        return HttpResponse(f"The average salary for Python developers in Bangalore is: {average_salary}")

    response_content = f'<p style="font-size: 1.2em;">The average salary for Python developers in Bangalore is: <strong>{avg_salary}</strong></p>'
    return HttpResponse(response_content)



