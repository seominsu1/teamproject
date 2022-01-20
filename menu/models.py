from django.db import models

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=45)
    price=models.IntegerField()
    img=models.CharField(max_length=45)
    ingredient=models.CharField(max_length=45)
    restaurant_id=models.IntegerField
