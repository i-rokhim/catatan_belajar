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

    def test_pengguna_tidak_bisa_edit_catatan_orang_lain(self):
        self.client.login(username="userA", password="rahasia123")
        catatan_b = Catatan.objects.get(judul="catatan milik B")
        response = self.client.get(reverse("edit_catatan", args=[catatan_b.pk]))
        self.assertEqual(response.status_code, 404)

    def test_pengguna_tidak_bisa_hapus_catatan_orang_lain(self):
        self.client.login(username="userA", password="rahasia123")
        catatan_b = Catatan.objects.get(judul="catatan milik B")
        response = self.client.post(reverse("hapus_catatan", args=[catatan_b.pk]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Catatan.objects.filter(pk=catatan_b.pk).exists())

    def test_belum_login_dialihkan_ke_login(self):
        response = self.client.get(reverse("daftar_catatan"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("login", response.url)

    def test_catatan_memiliki_prioritas_default(self):
        catatan_a = Catatan.objects.get(judul="catatan milik A")
        self.assertEqual(catatan_a.prioritas, "Normal")

    def test_prioritas_yang_dipilih_tersimpan_ke_database(self):
        self.client.login(username="userA", password="rahasia123")
        self.client.post(reverse("tambah_catatan"), {"judul": "belajar testing", "kategori": "Django", "prioritas": "Tinggi", "isi": "isi catatan"})
        catatan_baru = Catatan.objects.get(judul="belajar testing")
        self.assertEqual(catatan_baru.prioritas, "Tinggi")

    def test_filter_prioritas_hanya_menampilkan_yang_cocok(self):
        self.client.login(username="userA", password="rahasia123")

        Catatan.objects.create(
            judul="Judul Satu",
            kategori="tes",
            prioritas="Tinggi",
            isi="isi catatan",
            pemilik=self.a
        )

        Catatan.objects.create(
            judul="Judul Dua",
            kategori="tes",
            prioritas="Normal",
            isi="isi catatan",
            pemilik=self.a
        )

        response = self.client.get(
            reverse("daftar_catatan"),
            {"prioritas": "Tinggi"}
        )

        self.assertContains(response, "Judul Satu")
        self.assertNotContains(response, "Judul Dua")