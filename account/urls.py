from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout,name='logout'),
    path('sendmail/',views.sendmail,name='sendmail'),
    path('mail',views.checkmail,name='checkmail'),
]