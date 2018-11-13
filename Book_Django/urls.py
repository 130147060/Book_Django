import xadmin
from django.conf.urls import url, include

from Apps.book_main import views

urlpatterns = [
    url('^$', views.first_page,name='/'),
    url('account/', include('Apps.book_account.urls')),
    url('page/',include('Apps.book_search.urls')),
    url('detail/',include('Apps.book_detail.urls')),
    url('car/',include('Apps.book_car.urls')),
    url('pay/',include('Apps.book_pay.urls')),
    url('register/',include('Apps.email_register.urls')),
    url('xadmin/',xadmin.site.urls)
]
