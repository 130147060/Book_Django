

from django.conf.urls import url

from Apps.book_detail import views

urlpatterns = [
    url('detail/',views.detail_view,name='detail_view')
]
