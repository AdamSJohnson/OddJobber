from django.conf.urls import url

from . import views

urlpatterns = [
    url('createJob/', views.createJob, name='Jobs'),
]