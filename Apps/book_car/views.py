import random

from django.db.models import F
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from Apps.book_account.context_processors import shop_count
from Apps.book_main.models import Shopcar, Book_lists, OrderList


def convert_dict(a,b):
    return dict(zip(a,b))


@csrf_exempt
def add_view(request):
    if request.is_ajax():
        if request.user.is_authenticated():
            try:
                uid=request.user.userprofile.uid
                book_id=int(request.POST.get('book_id'))
                number=int(request.POST.get('number'))
                car=Shopcar.objects.filter(uid=uid,book_id_id=book_id,status=1).first()
                if car:
                    car.number=F('number')+number
                    car.save(update_fields=['number'])
                else:
                    car=Shopcar(uid_id=uid,number=number,book_id_id=book_id)
                    car.save()
                data=shop_count(request)
                data['status']=200
                data['msg']='su ccess'
                return JsonResponse(data=data)
            except :
                return JsonResponse(data={'status':404,'msg':'error'})

        else:
            return JsonResponse(data={'status':414,'msg':'place login'})

    else:
        pass
@login_required
def shop_car(request):
    if request.method=='GET':
        uid = request.user.userprofile.uid
        lists=Shopcar.objects.filter(uid_id=uid,status=1)
        for list in lists:
            list.name=Book_lists.objects.filter(book_id=list.book_id_id).values('book_name').first()['book_name']
            list.price=50
        return render(request,'shop_car.html',{'lists':lists})
def order(request):
    total_quantity=0
    order_code = str(random.randint(100000000, 999999999))
    uid = request.user.userprofile.uid
    dict_one=request.POST.getlist('book_ids')
    dict_two=[]
    for dict in dict_one:
        dict_two.append(eval(dict))
    number_one=request.POST.getlist('number')
    number_two=[]
    for number in number_one:
        number_two.append(eval(number))
    id_one=request.POST.getlist('book_id')
    id_two=[]
    for id in  id_one:
        id_two.append(eval(id))
    dict=convert_dict(id_two,number_two)
    object_one=[]
    for book_id in dict_two:
        buy_book_number=dict[book_id]
        total_quantity+=buy_book_number
        car_book=Shopcar.objects.filter(uid_id=uid,book_id_id=book_id,status=1).first()
        car_book_number=car_book.number
        if car_book_number > buy_book_number :
            car_book.number=F('number')-buy_book_number
            car_book.save(update_fields=['number'])
        else:
            car_book.status=0
            car_book.save(update_fields=['status'])
        book_object=Book_lists.objects.filter(book_id=book_id).first()
        book_object.number=buy_book_number
        object_one.append(book_object)
        try:
            orderss=OrderList(uid_id=uid,number=buy_book_number,status=0,book_id_id=book_id,order_code=order_code)
            orderss.save()
        except Exception as e:
            print(e)
    order_one=OrderList.objects.filter(order_code=order_code)
    total_money=total_quantity*50
    for order_two in order_one:
        order_two.name=Book_lists.objects.filter(book_id=order_two.book_id_id).values('book_name').first()['book_name']
    return  render(request,'order_page.html',{'order_one':order_one,'total_money':total_money,'total_quantity':total_quantity,'order_code':order_code})



