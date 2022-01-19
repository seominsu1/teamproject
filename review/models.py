from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class reivewboard(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    star = models.CharField(max_length=100)
    contents = models.TextField()
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    create_data = models.DateTimeField(auto_now_add=True)