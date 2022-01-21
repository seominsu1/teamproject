from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#음식점 DB
class restaurant(models.Model) :
    name = models.CharField(max_length=200) #음식점 이름
    address = models.CharField(max_length=200)  #음식점 주소
    phonenum = models.CharField(max_length=200) #음식점 연락처
    time = models.CharField(max_length=200) #음식점 영업시간
    pic_url = models.CharField(max_length=200)  #음식점 사진 주소
    longitude = models.FloatField() #음식점 경도
    latitude = models.FloatField()  #음식점 위도
    latitude = models.FloatField()  # 음식점 위도
    large_cate=models.CharField(max_length=200) #음식점 대분류
    small_cate=models.CharField(max_length=200) #음식점 소분류

class comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contents=models.TextField()
    star=models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    restaurant=models.ForeignKey(restaurant,on_delete=models.CASCADE)