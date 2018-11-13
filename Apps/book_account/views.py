
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Apps.book_account import tasks
from Apps.book_main.models import UserProfile

def register_view(request):
    if request.method=='GET':
        return render(request,'book_register.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        phone=request.POST.get('phone')
        if User.objects.filter(username=username):
            return render(request, 'book_register.html', {'msg': '用户已存在'})
        else:
            user = User.objects.create_user(username=username,
                                            password=password
                                            )
            uid = user.id
            userprofile = UserProfile.objects.create(phone=phone, user_id=uid,)
            tasks.say_hello.delay(uid)
            return HttpResponse(u"邮件发送成功， 请查收")
def login_view(request):
    if request.method=='GET':
        return render(request,'book_login.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        password_again=request.POST.get('password_again')
        if password_again!=password:
            return render(request, 'book_login.html', {'msg': '两次密码不一致'})
        else:
            user = authenticate(request, username=username, password=password)
            uid=user.id
            if user :
                user_main=UserProfile.objects.filter(user_id=uid).first()
                print(user_main.status)
                if user_main.status == 1:
                    login(request, user)
                    return redirect('/')
                else:
                    return render(request, 'book_login.html', {'msg': '请激活账号'})
            else:
                return render(request, 'book_login.html', {'msg': '账号密码错误'})

def logout_view(request):
    logout(request)
    return redirect('/')
