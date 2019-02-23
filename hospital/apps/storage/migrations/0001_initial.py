# Generated by Django 2.1.5 on 2019-02-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruku_info',
            fields=[
                ('insertTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('opertionTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('isdelete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('ruku_id', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='入库id')),
                ('ruku_time', models.CharField(max_length=30, verbose_name='入库时间')),
                ('drug_id', models.CharField(max_length=30, verbose_name='药品id')),
                ('drug_name', models.CharField(max_length=30, verbose_name='商品名称')),
                ('drug_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='药品单价')),
                ('ruku_drugcount', models.IntegerField(default=0, verbose_name='入库药品数量')),
                ('yruku', models.IntegerField(default=0, verbose_name='应入库药品数量')),
                ('sruku', models.IntegerField(default=0, verbose_name='实入库药品数量')),
                ('hwh', models.CharField(max_length=50, verbose_name='货位号')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
