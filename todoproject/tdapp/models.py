from django.db import models

# Create your models here.
class task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.TextField()
    date=models.DateField('yyyy-mm-dd')
def __str__(self):
    return self.name
