from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(default='')
    description = models.TextField(default='')
    zipcode = models.CharField(default='')
    price = models.DecimalField(max_digits=2)
    # tags: TODO
    due_date = models.DateField()
    # creator: user TODO