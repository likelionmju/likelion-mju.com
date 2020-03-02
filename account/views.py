from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import User
import random
from datetime import datetime
from django.utils import timezone

def login(request):
    if request.method =='POST':
        id = request.POST['id']
        pw = request.POST['pw']
        user = auth.authenticate(request,username=id,password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        if request.POST['pw'] == request.POST['pw2']:
            user = User.objects.create_user(
                email = request.POST['email'],
                number = request.POST['id'],
                name = request.POST['name'],
                gender=request.POST['gender'],
                phone = request.POST['phone_number'],
                college=request.POST['college'],
                department = request.POST['department'],
                grade = request.POST['grade'][0],
                password = request.POST['pw'],
                rand = randstr(10),
                user_is_active = False,
            )
            message = user.name + "님께서 입력하신 메일로 인증링크를 발송했습니다."
            return render(request,'notify.html',{'message':message})
    return render(request, 'register.html')

def logout(request):
        auth.logout(request)
        return redirect('login')

def sendmail(request):
        html_message = render_to_string('sendmail.html')
        email = EmailMessage('title',html_message,to=['choiys0311@gmail.com'])
        email.content_subtype = "html"
        email.send()
        message = "님께서 입력하신 메일로 인증링크를 발송했습니다."
        return render(request,'notify.html',{'message':message})


def checkmail(request):
        User.user_is_active = True
        User.rand=''
        message = "이메일이 인증되었습니다."
        return redirect('www.naver.com',{'message':message})

#random
def randstr(length):
        rstr = "0123456789abcdefghijklnmopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ"
        rstr_len = len(rstr) - 1
        result = ""
        for i in range(length):
            result += rstr[random.randint(0, rstr_len)]
        return result

