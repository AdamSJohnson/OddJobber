from django.conf.urls import url

from . import views

urlpatterns = [
    url('createJob/', views.createJob.as_view(), name='jobs'),
    url('listJobs/', views.listJobs, name='listJobs'),
]