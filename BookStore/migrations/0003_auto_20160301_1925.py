# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-01 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u4e66\u540d'),
        ),
    ]
