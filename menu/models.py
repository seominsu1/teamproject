from django.db import models
from restaurant.models import restaurant

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=200)    #메뉴이름
    general_name=models.CharField(max_length=200) #영양정보를 위한 메뉴이름
    price=models.IntegerField()             #메뉴가격
    img_url=models.CharField(max_length=200)     #이미지
    ingredient=models.CharField(max_length=200) #재료
    restaurant=models.ForeignKey(restaurant,on_delete=models.CASCADE)

