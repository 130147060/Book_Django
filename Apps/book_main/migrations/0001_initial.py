# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-13 09:06
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_details',
            fields=[
                ('detail_id', models.AutoField(primary_key=True, serialize=False, verbose_name='详情ID')),
                ('srction_book', models.CharField(max_length=225, verbose_name='章节')),
                ('book_detail', models.TextField(max_length=2000, verbose_name='详情')),
            ],
            options={
                'verbose_name': '小说详情',
                'verbose_name_plural': '小说详情',
                'db_table': 'Book_details',
            },
        ),
        migrations.CreateModel(
            name='Book_kinds',
            fields=[
                ('kind_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='种类ID')),
                ('kind_name', models.CharField(max_length=255, unique=True, verbose_name='类别')),
            ],
            options={
                'verbose_name': '小说种类',
                'db_table': 'Book_kinds',
            },
        ),
        migrations.CreateModel(
            name='Book_lists',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='书ID')),
                ('img_url', models.CharField(max_length=255, null=True, verbose_name='图片链接')),
                ('book_name', models.CharField(max_length=225, null=True, unique=True, verbose_name='书名')),
                ('author_name', models.CharField(max_length=225, null=True, verbose_name='作者')),
                ('book_intro', models.TextField(max_length=2000, verbose_name='简介')),
                ('kind_id', models.ForeignKey(db_column='kind_id', on_delete=django.db.models.deletion.DO_NOTHING, to='book_main.Book_kinds', verbose_name='种类ID')),
            ],
            options={
                'verbose_name': '小说列表',
                'verbose_name_plural': '小说列表',
                'db_table': 'Book_lists',
            },
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '找回密码')], max_length=255, verbose_name='验证码类型')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
                'db_table': 'activate',
            },
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False, verbose_name='订单ID')),
                ('status', models.IntegerField(default=1, verbose_name='订单状态')),
                ('number', models.IntegerField(default=0, verbose_name='商品数量')),
                ('order_code', models.CharField(default='000000', max_length=255, verbose_name='订单号')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book_main.Book_lists', verbose_name='商品ID')),
            ],
            options={
                'verbose_name': '订单列表',
                'verbose_name_plural': '订单列表',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Shopcar',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False, verbose_name='购物车ID')),
                ('number', models.IntegerField(default=0, verbose_name='商品数量')),
                ('status', models.IntegerField(default=1, verbose_name='商品状态')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book_main.Book_lists', verbose_name='商品ID')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
                'db_table': 'shopcar',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('phone', models.CharField(max_length=11)),
                ('uid', models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('status', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
        ),
        migrations.AddField(
            model_name='shopcar',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='book_main.UserProfile', verbose_name='用户ID'),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='book_main.Shopcar', verbose_name='用户ID'),
        ),
        migrations.AddField(
            model_name='book_details',
            name='book_id',
            field=models.ForeignKey(db_column='book_id', on_delete=django.db.models.deletion.DO_NOTHING, to='book_main.Book_lists', verbose_name='详情'),
        ),
    ]
