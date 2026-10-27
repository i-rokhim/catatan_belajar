from django.shortcuts import render, redirect
from .models import Catatan
from .forms import CatatanForm


def daftar_catatan(request):
    semua = Catatan.objects.order_by('-tanggal')
    return render(request, 'catatan/daftar.html', {'semua': semua})


def tambah_catatan(request):
    if request.method == 'POST':
        form = CatatanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_catatan')
    else:
        form = CatatanForm()
    return render(request, 'catatan/tambah.html', {'form': form})