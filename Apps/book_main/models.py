import datetime
import random

from django.db import models

# Create your models here.

class Book_kinds(models.Model):
    kind_id=models.IntegerField('种类ID',primary_key=True)
    kind_name=models.CharField('类别',max_length=255,null=False,unique=True)
    class Meta:
        verbose_name = u"小说种类"
        db_table='Book_kinds'

class Book_lists(models.Model):
    book_id=models.IntegerField('书ID',primary_key=True)
    img_url=models.CharField('图片链接',max_length=255,null=True)
    book_name=models.CharField('书名',max_length=225,null=True,unique=True)
    author_name=models.CharField('作者',max_length=225,null=True)
    book_intro=models.TextField('简介',max_length=2000)
    kind_id=models.ForeignKey('Book_kinds',models.DO_NOTHING,db_column='kind_id',db_index=True,verbose_name='种类ID')
    class Meta:
        verbose_name = u"小说列表"
        verbose_name_plural = verbose_name
        db_table='Book_lists'
class Book_details(models.Model):
    detail_id=models.AutoField('详情ID',primary_key=True)
    srction_book=models.CharField('章节',max_length=225)
    book_detail=models.TextField('详情',max_length=2000)
    book_id=models.ForeignKey('Book_lists',models.DO_NOTHING,db_column='book_id',db_index=True,verbose_name='详情')
    class Meta:
        verbose_name = u"小说详情"
        verbose_name_plural = verbose_name
        db_table='Book_details'

class UserProfile(models.Model):
    phone = models.CharField(max_length=11)
    uid = models.AutoField('用户ID', primary_key=True)
    user = models.OneToOneField('auth.User')
    status=models.IntegerField(default=0)
    class Meta:
        db_table = 'user_profile'

class Shopcar(models.Model):
    car_id = models.AutoField('购物车ID', primary_key=True)
    number = models.IntegerField('商品数量', default=0)
    book_id = models.ForeignKey(Book_lists, models.DO_NOTHING,verbose_name='商品ID')
    uid = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='uid', verbose_name='用户ID')
    status = models.IntegerField(default=1,verbose_name='商品状态')
    class Meta:
        verbose_name = u"购物车"
        verbose_name_plural = verbose_name
        db_table = 'shopcar'

class OrderList(models.Model):
    order_id=models.AutoField('订单ID',primary_key=True)
    uid = models.ForeignKey('Shopcar', models.DO_NOTHING, db_column='uid', verbose_name='用户ID')
    status=models.IntegerField('订单状态',default=1)
    book_id = models.ForeignKey('Book_lists', models.DO_NOTHING,verbose_name='商品ID')
    number = models.IntegerField('商品数量', default=0)
    order_code=models.CharField(max_length=255,default='000000',verbose_name='订单号')
    class Meta:
        verbose_name = u"订单列表"
        verbose_name_plural = verbose_name
        db_table = 'order'

from django.db import models


class EmailVerifyRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # 包含注册验证和找回验证
    send_type = models.CharField(verbose_name=u"验证码类型", max_length=255, choices=(("register",u"注册"), ("forget",u"找回密码")))
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.datetime.now)
    class Meta:
        db_table = 'activate'
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name
