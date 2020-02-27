from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import page.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page.views.home),
]

urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)