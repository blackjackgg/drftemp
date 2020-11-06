# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# def myvalid(data):
#     return False



# Create your models here.
class Task(models.Model):
    q = models.CharField('q', max_length=30,default="222")              ##外键引用 app_name = models.ForeignKey("cmdb.App",related_name='deploy_app', verbose_name="App")
    a = models.CharField('a', max_length=30,default="222")
    link = models.CharField('link', max_length=30,default="222",)
    date = models.DateTimeField('date',auto_now=True)
    choice=models.BooleanField("choice")
    myfile=models.FileField("myfile",upload_to="myfile")
    myimg=models.ImageField("myimg",upload_to="img")

    class Meta:  ##独立新表
        db_table='Task'
        verbose_name = "任务"


    def __str__(self):
        return self.q


# Create your models here.


#modal类型
#BooleanField（）
# CharField(max_length=none[, **options])
# DateField  DateTimeField([auto_now=False, auto_now_add=False, **options])
# DecimalField（max_digits=None，decimal_places=None[, **options]） 小数点
# BinaryField
#ImageField([upload_to=None, height_field=None, width_field=None, max_length=100, **options]) 需要安装pillow模块
#EmailField([maxlength=75, **options])
#FileField(upload_to=None[, max_length=100, **options])  默认的form widget 是 FileInput
#FloatField
#IntegerField #整数
#IPAddressField
#GenericIPAddressField
#NullBooleanField
#PositiveIntegerField 正证书
#SlugField url常用  只能包含字母，数字，下划线和连字符的字符串
#TextField 大文本
#TimeField
#URLField
#FilePathField(path=None[, match=None, recursive=False, max_length=100， options])

#field字段内容
#editable  #error_messages  #help_text  primary_key  radio_admin  unique
#unique_for_date  #unique_for_month / unique_for_year
#validators
#db_index=True 创建索引
#verbose_name  string类型。更人性化的列名。






