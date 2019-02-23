from django.db import models
from utils.basemodel import BaseModel
# Create your models here.

class Suppier(BaseModel) :
    suppierId=models.CharField(max_length=10,primary_key=True,verbose_name="供应商id")
    name=models.CharField(max_length=50,verbose_name="名字")
    phoneNo=models.CharField(max_length=12,verbose_name="电话号")
    address=models.CharField(max_length=100,verbose_name="地址")
    linkMan=models.CharField(max_length=50,verbose_name="联系人")