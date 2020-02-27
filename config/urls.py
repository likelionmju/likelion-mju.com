from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import page.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(page.urls)),
]

urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)