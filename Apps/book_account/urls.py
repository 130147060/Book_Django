

from django.conf.urls import url

from Apps.book_account import views

urlpatterns = [
    url('register/', views.register_view,name='register_view'),
    url('login/',views.login_view,name='login_view'),
    url('logout/',views.logout_view,name='logout_view')
]
