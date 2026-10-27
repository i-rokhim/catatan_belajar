from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrasi, name='registrasi'),
]