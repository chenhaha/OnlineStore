# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-16 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0023_auto_20160316_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
