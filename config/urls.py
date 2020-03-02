from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import page.urls, account.urls
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(page.urls)),
    path('account/', include(account.urls)),
]

urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)