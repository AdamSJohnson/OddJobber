from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(default='', max_length=140)
    description = models.TextField(default='')
    zipcode = models.CharField(default='', max_length=10)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    # tags: TODO
    due_date = models.DateField()
    # creator: user TODO