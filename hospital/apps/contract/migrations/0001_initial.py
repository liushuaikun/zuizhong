# Generated by Django 2.1.5 on 2019-02-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='drugsuppier',
            fields=[
                ('insertTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('opertionTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('isdelete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('suppierId', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='供应商id')),
                ('drugId', models.CharField(max_length=10, verbose_name='药品id')),
                ('price', models.IntegerField(default=0, verbose_name='药品单价')),
                ('amount', models.IntegerField(default=0, verbose_name='药品数量')),
                ('userId', models.CharField(max_length=10, verbose_name='用户id')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='交易时间')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
