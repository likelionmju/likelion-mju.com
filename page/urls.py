from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply, name='apply'),
    path('apply/complete/', views.complete, name='complete'),
    path('intro', views.intro, name='intro'),
]