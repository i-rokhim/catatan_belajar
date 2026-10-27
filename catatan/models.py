from django.db import models


class Catatan(models.Model):
    judul = models.CharField(max_length=200)
    kategori = models.CharField(max_length=100)
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul

# Create your models here.
