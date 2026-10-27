from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_catatan, name='daftar_catatan'),
    path('tambah/', views.tambah_catatan, name='tambah_catatan'),
    path('edit/<int:pk>/', views.edit_catatan, name='edit_catatan'),
    path('hapus/<int:pk>/', views.hapus_catatan, name='hapus_catatan'),
]