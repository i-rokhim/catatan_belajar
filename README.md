# Catatan Belajar Coding

Aplikasi catatan belajar sederhana dengan Django. Setiap pengguna punya akun
sendiri dan hanya melihat catatannya sendiri.

## Fitur
- Tambah, lihat, edit, dan hapus catatan (judul, kategori, isi, tanggal)
- Registrasi, login, dan logout
- Catatan dibatasi per pengguna
- Pencarian catatan berdasarkan judul
- Prioritas catatan dengan pilihan tingkat kepentingan Rendah, Normal, atau Tinggi

## Menjalankan di Windows (CMD)
    
    cd C:\catatan_belajar
    python -m venv venv
    venv\Scripts\activate
    pip install django
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Buka http://127.0.0.1:8000/ di browser.

## Menjalankan tes
    
    python manage.py test

Tes memastikan pengguna hanya melihat catatannya sendiri, tidak bisa mengedit atau menghapus catatan orang lain, pencarian berjalan, nilai bawaan prioritas adalah Normal, serta prioritas yang dipilih dari formulir tersimpan ke database.

## Catatan
- `db.sqlite3` tidak ikut git, jadi database dibuat ulang lewat `migrate`.
- Halaman admin: http://127.0.0.1:8000/admin/

## Demo

alamatku https://irokhim.pythonanywhere.com

situs berjalan di paket gratis PythonAnywhere dan bisa nonaktif kalau tidak diperpanjang tiap bulan.

