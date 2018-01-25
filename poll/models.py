from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(verbose_name='书名', max_length=200, default='', unique=True)
    publisher = models.IntegerField(verbose_name='出版社ID', default=0)
    isbn = models.CharField(verbose_name='银行卡号', max_length=30, default='')
    category = models.IntegerField(verbose_name='分类ID', default=0)
    pages = models.IntegerField(verbose_name='书箱页数', default=0)
    publish_at = models.DateField(verbose_name='出版日期')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        db_table = 'book'
        verbose_name = '图书表'
        verbose_name_plural = verbose_name

