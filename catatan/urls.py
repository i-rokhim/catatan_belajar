from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_catatan, name='daftar_catatan'),
    path('tambah/', views.tambah_catatan, name='tambah_catatan'),
]