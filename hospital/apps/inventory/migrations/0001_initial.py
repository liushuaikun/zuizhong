# Generated by Django 2.1.5 on 2019-02-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Druglists',
            fields=[
                ('insertTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('opertionTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('isdelete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('drugid', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='药品ID')),
                ('name', models.CharField(max_length=50, verbose_name='药品名称')),
                ('type', models.CharField(max_length=256, verbose_name='药品种类')),
                ('explain', models.CharField(max_length=256, verbose_name='药品说明')),
                ('birth', models.CharField(max_length=256, verbose_name='药品生产日期')),
                ('scrap', models.CharField(max_length=256, verbose_name='药品过期日期')),
                ('spec', models.CharField(max_length=256, verbose_name='药品规格')),
                ('drugnum', models.IntegerField(default=0, verbose_name='药品数量')),
                ('export', models.IntegerField(default=0, verbose_name='日出库量')),
                ('hwh', models.CharField(max_length=50, verbose_name='货位号')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
