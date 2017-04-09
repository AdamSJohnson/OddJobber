from django.db import models
from taggit.managers import TaggableManager

class Tag(models.Model):
    name = models.CharField(default='', max_length=20)

class Job(models.Model):
    jobtitle = models.CharField(default='', max_length=140)
    description = models.TextField(default='')
    zipcode = models.CharField(default='', max_length=10)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    tags = TaggableManager()
    due_date = models.CharField(default='', max_length=10)
    # creator: user TODO