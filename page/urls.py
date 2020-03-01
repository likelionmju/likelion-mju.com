from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply, name='apply'),
    path('account/',include('account.urls'),name="account"),
]