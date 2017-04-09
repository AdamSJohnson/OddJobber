from django.conf.urls import url
from . views import search_jobs, create_job, list_jobs

urlpatterns = [
    url('create_job/', create_job.as_view(), name='create_jobs'),
    url('list_jobs/', list_jobs, name='list_jobs'),
    url('search_jobs/', search_jobs, name='search_jobs'),
]