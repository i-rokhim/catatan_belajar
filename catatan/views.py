from django.shortcuts import render
from .models import Catatan


def daftar_catatan(request):
    semua = Catatan.objects.order_by('-tanggal')
    return render(request, 'catatan/daftar.html', {'semua': semua})

# Create your views here.
