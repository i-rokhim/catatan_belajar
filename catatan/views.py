from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Catatan
from .forms import CatatanForm


@login_required
def daftar_catatan(request):
    semua = Catatan.objects.filter(pemilik=request.user).order_by('-tanggal')
    return render(request, 'catatan/daftar.html', {'semua': semua})


@login_required
def tambah_catatan(request):
    if request.method == 'POST':
        form = CatatanForm(request.POST)
        if form.is_valid():
            catatan = form.save(commit=False)
            catatan.pemilik = request.user
            catatan.save()
            return redirect('daftar_catatan')
    else:
        form = CatatanForm()
    return render(request, 'catatan/tambah.html', {'form': form})


@login_required
def edit_catatan(request, pk):
    catatan = get_object_or_404(Catatan, pk=pk, pemilik=request.user)
    if request.method == 'POST':
        form = CatatanForm(request.POST, instance=catatan)
        if form.is_valid():
            form.save()
            return redirect('daftar_catatan')
    else:
        form = CatatanForm(instance=catatan)
    return render(request, 'catatan/edit.html', {'form': form})


@login_required
def hapus_catatan(request, pk):
    catatan = get_object_or_404(Catatan, pk=pk, pemilik=request.user)
    if request.method == 'POST':
        catatan.delete()
        return redirect('daftar_catatan')
    return render(request, 'catatan/hapus.html', {'catatan': catatan})


def registrasi(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('daftar_catatan')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrasi.html', {'form': form})