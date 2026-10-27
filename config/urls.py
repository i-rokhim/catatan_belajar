from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('akun/', include('django.contrib.auth.urls')),
    path('akun/daftar/', include('catatan.urls_akun')),
    path('', include('catatan.urls')),
]