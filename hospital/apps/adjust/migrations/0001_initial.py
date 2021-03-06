# Generated by Django 2.1.5 on 2019-02-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adjustprice',
            fields=[
                ('adjustpriceID', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='调价单单号')),
                ('adjustdrugname', models.CharField(max_length=100, verbose_name='调价药品名称')),
                ('adjustpricebefore', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='调价前价格')),
                ('adjustpriceafter', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='调价后价格')),
                ('drugID', models.CharField(max_length=100, verbose_name='药品ID')),
            ],
        ),
    ]
