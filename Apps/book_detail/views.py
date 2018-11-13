import random


from django.shortcuts import render

# Create your views here.
from Apps.book_main.models import Book_details, Book_kinds, Book_lists


def detail_view(request):
    navigations = Book_kinds.objects.all()
    book_id=request.GET.get('book_id')
    kind_id=Book_lists.objects.filter(book_id=book_id).values('kind_id').first()
    k_id=kind_id.get('kind_id')
    kind=Book_kinds.objects.filter(kind_id=k_id).first()
    book=Book_lists.objects.filter(book_id=book_id).first()
    book.price=50
    book_details=Book_details.objects.filter(book_id=book_id)
    return render(request,'book_detail.html',{'book_details':book_details,'navigations':navigations,'book':book,'kind':kind})