from django.db import models

# Create your models here.
class restaurant(models.Model) :
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phonenum = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    pic = models.ImageField

