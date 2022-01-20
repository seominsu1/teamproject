from django.db import models

# Create your models here.
class Fruits(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()