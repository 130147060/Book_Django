from django.shortcuts import render
from django.db.models import Q

from Apps.book_main.models import *


def first_page(request):
    kind_id=request.GET.get('kind_id')
    navigations=Book_kinds.objects.all()
    # recombooks=Book_lists.objects.filter(Q(kind_id=11)
    #                                      |Q(kind_id=12))
    if kind_id:
        recombooks=Book_lists.objects.filter(kind_id=kind_id)
        book_kind=Book_kinds.objects.filter(kind_id=kind_id).first()
        return render(request, 'first_page.html', {'navigations': navigations, 'recombooks': recombooks,'book_kind':book_kind})
    else:
        recombooks=Book_lists.objects.all()
    return render(request,'first_page.html',{'navigations':navigations,'recombooks':recombooks})

