# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 03:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0008_auto_20160302_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='height',
        ),
        migrations.RemoveField(
            model_name='book',
            name='width',
        ),
    ]