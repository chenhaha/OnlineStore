# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0017_auto_20160302_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(max_length=100, null=True, verbose_name='\u6587\u7ae0\u4ecb\u7ecd'),
        ),
    ]
