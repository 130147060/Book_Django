

from django.conf.urls import url

from Apps.email_register import views

urlpatterns = [
    url('activate/',views.activate,name='activate_view')
]
