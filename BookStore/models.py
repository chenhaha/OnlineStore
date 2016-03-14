#coding:utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    alipay = models.CharField(max_length=32, verbose_name='支付宝账号')
    #mycart = models.ForeignKey('Cart', verbose_name='购物车',null=True)

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
        #app_label = u'myapp'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Cart(models.Model):
    #bookname = models.CharField(max_length=128, verbose_name='书名')
    cart_id = models.CharField(max_length=50,null=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='添加日期')
    quantity = models.IntegerField(default=1, verbose_name='数量')
    book = models.ForeignKey('Book', unique=False, null=True)
    user = models.ForeignKey('User', unique=False, null=True)

    class META:
        db_table = 'cart_items'
        ordering = ['date_added']

    def total(self):
        return self.quantity * self.book.price

    def name(self):
        return self.book.name

    def __unicode__(self):
        return '购物车'