from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/createJobs$', views.createJob, name='Jobs'),
]