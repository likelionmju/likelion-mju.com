from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),
    path('home', views.home, name='home'),
    path('apply/', views.apply, name='apply'),
    path('apply/complete/', views.complete, name='complete'),
    path('apply/list/', views.list),
    path('apply/list/<str:opt>', views.list_opt, name='list'),
    path('apply/detail/<int:id>/', views.detail, name='detail'),
]