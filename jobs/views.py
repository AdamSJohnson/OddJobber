from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Job
from . import forms

class create_job(CreateView):
    model = Job
    success_url = '/home'
    form_class = forms.JobForm

def search_jobs(request):
    pass

def list_jobs(request):
    def validateJobSearch(request):
        pass

    error_string = None
    if request.method == "POST":
        error_string = validateJobSearch(request)
        if error_string is not None:
            jobs_list = Job.objects.all()
            return render(request, 'list_jobs.html', {'jobs': jobs_list})
    return render(request, 'search_jobs.html', {'error_string': error_string})