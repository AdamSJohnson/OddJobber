from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Job
from . import forms

class createJob(CreateView):
    model = Job
    success_url = '/home'
    form_class = forms.JobForm


def listJobs(request):
    def validateJobSearch(request):
        pass

    error_string = None
    if request.method == "POST":
        error_string = validateJobSearch(request)
        if error_string is not None:
            jobs_list = Job.objects.all()
            return render(request, 'listJobs.html', {'jobs': jobs_list})
    return render(request, 'searchJobs.html', {'error_string': error_string})