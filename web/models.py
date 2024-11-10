from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField(max_length=20)
    tel = models.IntegerField(max_length=11)

