from django.db.models import Q
from django.shortcuts import render, redirect


# Create your views here.
from Apps.book_main.models import Book_lists, Book_kinds


def search_view(request):
    search_key=request.POST.get('search_key')
    navigations = Book_kinds.objects.all()
    if search_key=='':
        return redirect('/')
    else:
        if search_key.isdigit():
            search_books = Book_lists.objects.filter(book_id=int(search_key))
        else:
            search_books = Book_lists.objects.filter( Q(book_name__contains=search_key)
                                                     |Q(book_intro__contains=search_key))
        return render(request, 'search_page.html', {'search_books': search_books,'navigations':navigations})