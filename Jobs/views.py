from django.shortcuts import render
from django.http import HttpResponse


def createJob(request):
    return render(request, 'createJob.html')