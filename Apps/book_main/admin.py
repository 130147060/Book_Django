import xadmin
from django.contrib import admin
# Register your models here.
from xadmin import views

from Apps.book_main.models import *


class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    # 整体配置
    site_title = '小说电商平台管理系统'
    site_footer = 'Come From Gud'
    menu_style = 'accordion'  # 菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)

class Book_kind_one(object):
    # 后台列表显示列
    list_display = ['kind_id', 'kind_name']
    # 后台列表查询条件
    search_fields = ['kind_id', 'kind_name']
    list_per_page = 20


class Book_list_one(object):
    # 后台列表显示列
    list_display = ['book_id', 'img_url', 'book_name', 'author_name', 'book_intro', 'kind_id']
    # 后台列表查询条件
    search_fields = ['book_id', 'img_url', 'book_name', 'author_name', 'book_intro', 'kind_id']
    list_per_page = 20

class Book_detail_one(object):
    # 后台列表显示列
    list_display = ['detail_id', 'srction_book', 'book_detail','book_id']
    # 后台列表查询条件
    search_fields = ['detail_id', 'srction_book', 'book_detail','book_id']
    list_per_page = 20

class Shopcar_one(object):
    # 后台列表显示列
    list_display = ['car_id', 'number', 'book_id', 'uid', 'status']
    # 后台列表查询条件
    search_fields = ['car_id', 'number', 'book_id', 'uid', 'status']
    list_per_page = 20

class OrderList_one(object):
    # 后台列表显示列
    list_display = ['order_id', 'uid', 'status', 'book_id', 'number','order_code']
    # 后台列表查询条件
    search_fields = ['order_id', 'uid', 'status', 'book_id', 'number','order_code']
    list_per_page = 20

class EmailVerifyRecord_one(object):
    # 后台列表显示列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 后台列表查询条件
    search_fields = ['code', 'email', 'send_type', 'send_time']
    list_per_page = 20


xadmin.site.register(Book_kinds, Book_kind_one)
xadmin.site.register(Book_lists, Book_list_one)
xadmin.site.register(Book_details,Book_detail_one)
xadmin.site.register(Shopcar, Shopcar_one)
xadmin.site.register(OrderList, OrderList_one)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecord_one)
