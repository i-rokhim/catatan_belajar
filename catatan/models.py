from django.conf import settings
from django.db import models


class Catatan(models.Model):
    # Mendefinisikan pilihan tetap (Pilihan di database, Label yang tampil di form)
    PRIORITAS_CHOICES = [
        ('Rendah', 'Rendah'),
        ('Normal', 'Normal'),
        ('Tinggi', 'Tinggi'),
    ]
    judul = models.CharField(max_length=200)
    kategori = models.CharField(max_length=100)
    # Baris prioritas diubah dengan menambahkan parameter choices
    prioritas = models.CharField(max_length=20, choices=PRIORITAS_CHOICES, default='Normal')
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)
    pemilik = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.judul
        