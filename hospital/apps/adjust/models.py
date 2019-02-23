from django.db import models

# Create your models here.
class Adjustprice(models.Model):
    adjustpriceID = models.CharField(max_length=200,primary_key=True,verbose_name='调价单单号')
    adjustdrugname = models.CharField(max_length=100, verbose_name='调价药品名称')
    adjustpricebefore = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='调价前价格')
    adjustpriceafter = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='调价后价格')
    drugID = models.CharField(max_length=100, verbose_name='药品ID')