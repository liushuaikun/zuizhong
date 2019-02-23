# Generated by Django 2.1.5 on 2019-02-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suppier',
            fields=[
                ('insertTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('opertionTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('isdelete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('suppierId', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='供应商id')),
                ('name', models.CharField(max_length=50, verbose_name='名字')),
                ('phoneNo', models.CharField(max_length=12, verbose_name='电话号')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('linkMan', models.CharField(max_length=50, verbose_name='联系人')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
