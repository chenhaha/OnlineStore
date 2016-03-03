# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-01 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('author', models.CharField(max_length=128)),
                ('publish_date', models.DateField()),
                ('category', models.CharField(max_length=128)),
            ],
        ),
    ]
