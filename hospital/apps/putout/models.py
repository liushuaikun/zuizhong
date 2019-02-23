from django.db import models
from utils.basemodel import BaseModel
# Create your models here.
class Chuku_info(BaseModel):
    """出库药品信息"""
    chuku_id = models.CharField(max_length=30,primary_key=True, verbose_name='出库id')
    administrator_id = models.CharField(max_length=30, verbose_name='管理员id')
    department_id = models.CharField(max_length=30, verbose_name='部门id')
    drug_id = models.CharField(max_length=30, verbose_name='药品id')
    drug_name = models.CharField(max_length=30, verbose_name='商品名称')
    chuku_time = models.DateField(auto_now=True, verbose_name='出库时间')
    chuku_drugnumber = models.IntegerField(default=0, verbose_name='出库药品数量')
    hwh = models.CharField(verbose_name="货位号", max_length=50)