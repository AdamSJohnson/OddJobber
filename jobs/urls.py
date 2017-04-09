from django.conf.urls import url

from . import views

urlpatterns = [
    url('create_job/', views.create_job.as_view(), name='create_jobs'),
    url('list_jobs/', views.list_jobs, name='list_jobs'),
    url('search_jobs/', views.search_jobs, name='search_jobs'),
]