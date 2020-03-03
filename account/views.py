from django.shortcuts import render, redirect, get_object_or_404
# auth module
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import auth
# email module
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

def login(request):
    context = {}
    if request.method =='POST':
        if User.objects.filter(number=request.POST['id']).exists():
            user = User.objects.get(number=request.POST['id'])
            if check_password(request.POST['pw'], user.password):
                auth.login(request, user)
                if user.is_active:
                    return redirect('apply')
                else:
                    return redirect('home')
            else:
                context.update({'error':'incorrect password'})
        else:
            context.update({'error':'undefined user'})
    return render(request, 'login.html', context)

def logout(request):
        auth.logout(request)
        return redirect('login')

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
                password = request.POST['pw']
            )
            current_site = get_current_site(request)
            token = PasswordResetTokenGenerator().make_token(user)
            sendmail(user.email, {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token,
            })
            message = "입력하신 이메일로 인증링크를 발송하였습니다."
            return render(request, 'home.html', {'message':message})
    return render(request, 'register.html')

def sendmail(address, link):
    title = "멋쟁이사자처럼 at 명지대(서울) 계정 인증"
    html_message = render_to_string('mail_template.html', link)
    email = EmailMessage(title, html_message, to=[address])
    email.content_subtype = "html"
    email.send()

def authenticate(request, uidb64, token):
    pk = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=pk)
    if PasswordResetTokenGenerator().check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect('home')