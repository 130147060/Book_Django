

from django.conf.urls import url

from Apps.book_car import views

urlpatterns = [
    url('add/',views.add_view,name='add_view'),
    url('car/',views.shop_car,name='car_view'),
    url('order/',views.order,name='order_view')
]
