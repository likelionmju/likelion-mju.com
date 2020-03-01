from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def login(request):
    if request.method =='POST':
        id = request.POST['id']
        pw = request.POST['pw']
        user = auth.authenticate(request,username=id,password=pw)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        clientname = request.POST.get('name','')
        firstname = clientname[0]
        lastname = clientname[1:len(clientname)]
        if request.POST['pw'] == request.POST['pw2']:
            user = User.objects.create_user(email = request.POST['email'],username = request.POST['id'],password=request.POST['pw'],
            last_name = firstname, first_name= lastname)
            auth.login(request,user)
            return redirect('home')
    return render(request, 'register.html')



def logout(request):
        auth.logout(request)
        return redirect('login')

def checkmail(request):
        mailaddress = request.POST.get('email','')
        html_message = render_to_string('mail_template.html')
        email = EmailMessage('title', html_message, to=[ mailaddress ])
        email.content_subtype = "html"
        return email.send()


