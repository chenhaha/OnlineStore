# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-11 05:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0020_auto_20160310_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mycart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BookStore.Cart', verbose_name='\u8d2d\u7269\u8f66'),
        ),
    ]
