from django.conf.urls import url

from . import views

urlpatterns = [
    url('createJob/', views.createJob, name='jobs'),
    url('listJobs/', views.listJobs, name='listJobs'),
]