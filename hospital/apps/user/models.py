from django.db import models
from django.contrib.auth.models import AbstractUser
from utils import basemodel


# Create your models here.

class User(AbstractUser, basemodel.BaseModel):
    userID = models.CharField(max_length=30, primary_key=True, verbose_name="用户id")
    phone = models.CharField(max_length=30, verbose_name="联系电话")
