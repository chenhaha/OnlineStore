# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0015_book_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='nickname',
            field=models.CharField(max_length=128, null=True, verbose_name='\u82f1\u6587\u540d'),
        ),
    ]
