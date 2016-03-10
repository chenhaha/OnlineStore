# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 06:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0018_auto_20160302_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=128, verbose_name='\u4e66\u540d')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='\u6dfb\u52a0\u65e5\u671f')),
                ('quantity', models.IntegerField(default=1, verbose_name='\u6570\u91cf')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='mycart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BookStore.Cart', verbose_name='\u8d2d\u7269\u8f66'),
        ),
    ]
