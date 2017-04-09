from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.template import RequestContext
from .models import Job
from django.core.mail import send_mail
import datetime

from . import forms
class create_job(CreateView):
    model = Job
    success_url = '/home'
    form_class = forms.JobForm

def search_jobs(request):
    if request.method == "POST":
        bool_tokens = ['jobtitle', 'description', 'zipcode', 'tags', 'due_date']
        jobs_list = Job.objects.all()
        minDate = datetime.date(1, 1, 1)
        maxDate = datetime.date(9999, 12, 31)
        minPrice = 0.01
        maxPrice = 200
        for fieldval in request.POST:
            if fieldval in bool_tokens:
               newlist = jobs_list.filter(**{fieldval: request.POST.get(fieldval)})
               if newlist:
                  jobs_list = newlist
            if 'due_date_low' in request.POST:
                    minDate = request.POST.get('due_date_low')
            if 'due_date_high' in request.POST:
                    maxDate = request.POST.get('due_date_high')
                    newlist = jobs_list.filter(due_date__range= [minDate, maxDate])
                    if newlist:
                        jobs_list = newlist
            if 'price_low' in request.POST and request.POST.get('price_low') is not '':
                print("MinPrice = " + request.POST.get('price_low'))
                minPrice = request.POST.get('price_low')
                newlist = jobs_list.filter(price__range=[minPrice, maxPrice])
                if 'jobtitle' in request.POST:
                    newlist = newlist.filter(jobtitle__contains=request.POST.get('jobtitle'))
                if 'description' in request.POST:
                    newlist = newlist.filter(description__contains=request.POST.get('description'))
                if newlist:
                   jobs_list = newlist
            if 'email' in request.POST:
                email = request.POST.get('email')
                send_mail(
                    'Someone on OddJobber wants to work for you!',
                    'Check it out at OddJobber',
                    'oddjobber@oddjobber.me',
                    [email],
                    fail_silently=False,)
        return render(request, 'list_jobs.html', {'jobs': jobs_list}, RequestContext(request))
    return render(request, 'search_jobs.html', {'jobs': None}, RequestContext(request))

def list_jobs(request):
    def validateJobSearch(request):
        pass
    error_string = None
    if request.method == "POST":
        email = request.POST.get('email')
        print(email)
        error_string = validateJobSearch(request)
        if error_string is not None:
            return search_jobs(request)
        return search_jobs(request)
    return render(request, 'list_jobs.html', {'error_string': error_string})