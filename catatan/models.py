from django.conf import settings
from django.db import models


class Catatan(models.Model):
    judul = models.CharField(max_length=200)
    kategori = models.CharField(max_length=100)
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
        