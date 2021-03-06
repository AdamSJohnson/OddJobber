from django.forms import ModelForm
from . models import Job

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['jobtitle', 'description', 'price', 'zipcode', 'due_date', 'tags', "job_creator"]