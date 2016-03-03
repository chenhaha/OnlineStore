#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    alipay = models.CharField(max_length=32, verbose_name='支付宝账号')

    class Meta:
        ordering = ['-id']

    def __unicode__(self):
        return self.username


class Book(models.Model):
    name = models.CharField(max_length=128, verbose_name='书名')
    nickname = models.CharField(max_length=128, null=True, verbose_name='英文名',)
    desc = models.TextField( max_length=100, null=True, verbose_name='文章介绍', )
    picture = models.ImageField(upload_to='', blank=True, null=True, width_field='width', height_field='height',
                                verbose_name='图片')
    price = models.FloatField(verbose_name='价格')
    author = models.CharField(max_length=128, verbose_name='作者')
    publish_date = models.DateField(verbose_name='出版日期')
    category = models.CharField(max_length=128,verbose_name='分类')
    width = models.PositiveIntegerField(default=60, verbose_name='宽度')
    height = models.PositiveIntegerField(default=100, verbose_name='高度')

    class META:
        ordering = ['name']

    def __unicode__(self):
        return self.name