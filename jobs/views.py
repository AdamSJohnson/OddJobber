from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import models
from jobs.models import Job

def createJob(request):
    if request.method == "POST":
        title = request.POST.get("jobtitle")
        description = request.POST.get("description")
        price = request.POST.get("price")
        zipcode = request.POST.get('zipcode')
        duedate = request.POST.get('duedate')
        newjob = models.Job(title=title, description=description,
                            price=price, zipcode=zipcode, due_date=duedate)
        newjob.save()
        return HttpResponseRedirect('/jobs/createJob')
    return render(request, 'createJob.html')

def listJobs(request):
    jobs_list = Job.objects.all()
    return render(request, 'listJobs.html', {'jobs': jobs_list})