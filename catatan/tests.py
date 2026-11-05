from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Catatan


class DaftarCatatanTest(TestCase):
    def setUp(self):
        self.a = User.objects.create_user(username="userA", password="rahasia123")
        self.b = User.objects.create_user(username="userB", password="rahasia123")
        Catatan.objects.create(judul="catatan milik A", kategori="tes", isi="isi", pemilik=self.a)
        Catatan.objects.create(judul="catatan milik B", kategori="tes", isi="isi", pemilik=self.b)

    def test_pencarian_mencocokkan_judul(self):
        self.client.login(username="userA", password="rahasia123")
        Catatan.objects.create(judul="pelihara ayam", kategori="tes", isi="isi", pemilik=self.a)
        response = self.client.get(reverse("daftar_catatan"), {"q": "AYAM"})
        self.assertContains(response, "pelihara ayam")
        self.assertNotContains(response, "catatan milik A")

    def test_pengguna_hanya_melihat_catatan_sendiri(self):
        self.client.login(username="userA", password="rahasia123")
        response = self.client.get(reverse("daftar_catatan"))
        self.assertContains(response, "catatan milik A")
        self.assertNotContains(response, "catatan milik B")

