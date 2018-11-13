"""
自定义过滤器
1> 在app下新建templatetags的文件夹(名字必须是这个)
2> 在该文件下新建一个py文件
3> 实例化注册器
4> 声明过滤器(过滤器本质是一个函数)
5> 注册过滤器(两种:@register.filter   register.simple_tag)
6> 在需要使用过滤器的模板中引入过滤器{% load custom_filter %}  注意:添加完过滤器之后需要重启服务器
"""
from django import template

# 实例化注册器
register=template.Library()
'''
{{ value | multiply:params  }}
'''
@register.filter
def multiply(value,params):
    return value*params
'''
使用方法:
{% test 1 2 3 4 %}
'''
@register.simple_tag
def test(p1,p2,p3,p4):
    return p1+p2*p3+p4
