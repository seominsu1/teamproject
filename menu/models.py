from django.db import models
from restaurant.models import restaurant

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=45)    #메뉴이름
    price=models.IntegerField()             #메뉴가격
    img=models.CharField(max_length=45)     #이미지
    ingredient=models.CharField(max_length=45) #재료
    restaurant=models.ForeignKey(restaurant,on_delete=models.CASCADE)
