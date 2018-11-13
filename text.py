from django.contrib import admin

# Register your models here.


from xadmin import views

import xadmin

from APPS.account.models import Book, BookDetail, Classify
from APPS.dingdan.models import DingDan
from APPS.shopcar.models import Shopcar


class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 整体配置
    site_title = '小说电商平台管理系统'
    site_footer = 'Come From Father'
    menu_style = 'accordion'  # 菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)


class Book_kinds(object):
    # 后台列表显示列
    list_display = ['book_id', 'img_url', 'book_name', 'writer', 'miaoshu', 'classify_id']
    # 后台列表查询条件
    search_fields = ['book_id', 'img_url', 'book_name', 'writer', 'miaoshu', 'classify_id']
    list_per_page = 20


class Classifys(object):
    # 后台列表显示列
    list_display = ['classify_id', 'classify_name']
    # 后台列表查询条件
    search_fields = ['classify_id', 'classify_name']
    list_per_page = 20


class BookDetails(object):
    # 后台列表显示列
    list_display = ['zhangjie', 'text', 'book_id']
    # 后台列表查询条件
    search_fields = ['zhangjie', 'text', 'book_id']
    list_per_page = 20


class DingDans(object):
    # 后台列表显示列
    list_display = ['dd_id', 'dingdan_number', 'user_id', 'book_id', 'is_pay']
    # 后台列表查询条件
    search_fields = ['dd_id', 'dingdan_number', 'user_id', 'book_id', 'is_pay']
    list_per_page = 20


class Shopcars(object):
    # 后台列表显示列
    list_display = ['car_id', 'user_id', 'book_id', 'count', 'price', 'is_delete']
    # 后台列表查询条件
    search_fields = ['car_id', 'user_id', 'book_id', 'count', 'price', 'is_delete']
    list_per_page = 20


xadmin.site.register(Book, Books)
xadmin.site.register(Shopcar, Shopcars)
xadmin.site.register(DingDan, DingDans)
xadmin.site.register(BookDetail, BookDetails)
xadmin.site.register(Classify, Classifys)
