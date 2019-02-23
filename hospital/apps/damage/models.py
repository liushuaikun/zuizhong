from django.db import models
from utils.basemodel import BaseModel
# Create your models here.
class Breakagebefore(BaseModel):
    beforeID = models.CharField(max_length=200,primary_key=True,verbose_name="报损单ID")
    beforebrugname = models.CharField(max_length=100,verbose_name="报损药品名称")
    damagednum = models.IntegerField(default=0,verbose_name="损坏量")
    damagetime = models.DateTimeField(auto_now=True,verbose_name="报损时间")
    supplierID = models.CharField(max_length=100,verbose_name="供应商ID")
    pactID = models.CharField(max_length=100,verbose_name="合同ID")
    drugID = models.CharField(max_length=100, verbose_name='药品ID')