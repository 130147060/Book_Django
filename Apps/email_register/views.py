
from django.shortcuts import redirect, render

from Apps.book_main.models import EmailVerifyRecord, UserProfile



def activate(request):
    if request.method=='GET':
        code=request.GET.get('code')
        uid=request.GET.get('id')
        return render(request,'activate_view.html',{'code':code,'uid':uid})
    else:
        code=request.POST.get('code')
        uid=int(request.POST.get('uid'))
        all_records = EmailVerifyRecord.objects.filter(code=code)
        if all_records:
            user_active=UserProfile.objects.filter(uid=uid).first()
            user_active.status=1
            user_active.save(update_fields=['status'])
            return redirect('/account/login/')
        else:
            pass
