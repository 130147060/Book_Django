

from django.conf.urls import url

from Apps.book_pay import views

urlpatterns = [
    url('pay/',views.pay,name='pay_view'),
    url('notify/',views.notify_callback),
]
