from django.db import models

# Create your models here.
class Uploaddetails(models.Model):
    myfile=models.FileField(upload_to='')
    name=models.CharField(max_length=30)
    edu=models.CharField(max_length=100)
    spec=models.CharField(max_length=400)
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=10)