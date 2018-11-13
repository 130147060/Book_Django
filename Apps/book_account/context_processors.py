'''
如何定义全局的模板变量
1> app下新建一个context_processor文件
2> 在文件中创建一个函数,根据业务返回字典对象
3>注册,在settings中TEMPLATES添加
4>使用,直接  .字典的键
'''
from django.db.models import Sum


# 创建模板的全局变量
from Apps.book_main.models import Shopcar


def shop_count(request):
    count=0
    if request.user.is_authenticated():
        count = Shopcar.objects.filter(uid=request.user.userprofile.uid, status=1).aggregate(sum=Sum('number')).get('sum')
    return {'count':count}

