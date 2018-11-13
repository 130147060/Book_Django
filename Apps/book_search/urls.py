

from django.conf.urls import url

from Apps.book_search import views

urlpatterns = [
    url('search/',views.search_view,name='search_view')
]
