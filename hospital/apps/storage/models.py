from django.db import models
from utils.basemodel import BaseModel
# Create your models here.

class Ruku_info(BaseModel):
    """入库药品信息"""
    ruku_id = models.CharField(max_length=30,primary_key=True, verbose_name='入库id')
    ruku_time = models.CharField(max_length=30, verbose_name='入库时间')
    drug_id = models.CharField(max_length=30, verbose_name='药品id')
    drug_name=models.CharField(max_length=30,verbose_name='商品名称')
    drug_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='药品单价')
    ruku_drugcount = models.IntegerField(default=0, verbose_name='入库药品数量')
    yruku = models.IntegerField(default=0, verbose_name='应入库药品数量')
    sruku = models.IntegerField(default=0, verbose_name='实入库药品数量')
    hwh=models.CharField(verbose_name="货位号",max_length=50)
