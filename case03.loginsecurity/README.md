# Sistem Keamanan Akun dan Audit Log

## Deskripsi Program

Sistem Keamanan Akun dan Audit Log merupakan program sederhana berbasis Python untuk melakukan simulasi proses login pengguna. Program ini menerapkan validasi username dan password, pemeriksaan data akun, serta pencatatan hasil percobaan login.

Setiap percobaan login menampilkan waktu pengujian, username, status login, dan keterangan hasil validasi.

## Tujuan Program

Program ini bertujuan untuk memahami penerapan konsep pemrograman Python dalam proses validasi akun dan pencatatan aktivitas login. Konsep yang digunakan meliputi class, property, setter, decorator, regular expression, serta penanganan kesalahan menggunakan `try-except`.

## Fitur Program

* Validasi username minimal 5 karakter dan hanya menggunakan huruf atau angka.
* Validasi password minimal 8 karakter dan harus mengandung setidaknya satu angka.
* Pemeriksaan kecocokan username dan password dengan data pengguna.
* Pencatatan waktu dan hasil percobaan login.
* Penanganan kesalahan input dengan pesan yang sesuai.
* Empat skenario pengujian login.

## Penjelasan Program

### 1. Class `User`

Class `User` digunakan untuk menyimpan dan memvalidasi data pengguna. Username harus memiliki minimal lima karakter dan hanya berisi huruf atau angka. Password harus memiliki minimal delapan karakter dan mengandung setidaknya satu angka.

Jika input tidak memenuhi ketentuan, program akan menghasilkan `ValueError`.

### 2. Decorator `audit_log`

Decorator `audit_log` berfungsi mencatat dan menampilkan hasil setiap percobaan login. Informasi yang ditampilkan meliputi waktu pengujian, username, status login, dan keterangan.

Status login terdiri dari `BERHASIL` dan `DITOLAK`, sesuai dengan hasil pemeriksaan akun.

### 3. Fungsi `login_system`

Fungsi `login_system` digunakan untuk menjalankan proses login setelah validasi dilakukan. Fungsi ini menggunakan decorator `audit_log`, sehingga hasil setiap percobaan login dapat dicatat dan ditampilkan secara otomatis.

### 4. Fungsi `main`

Fungsi `main` merupakan bagian utama program. Fungsi ini menyimpan data pengguna dalam dictionary `database_users` dan menjalankan empat skenario pengujian menggunakan perulangan `for`.

### 5. Modul yang Digunakan

* `re` digunakan untuk memvalidasi format username dan memeriksa keberadaan angka dalam password.
* `datetime` digunakan untuk mencatat waktu percobaan login.
* `functools.wraps` digunakan untuk mempertahankan informasi fungsi asli pada decorator.

## Skenario Pengujian

Program menjalankan empat skenario pengujian berikut.

1. **Username tidak valid**

   Menggunakan username `yiran!` yang mengandung karakter khusus. Login ditolak karena username tidak memenuhi ketentuan.

2. **Password terlalu pendek**

   Menggunakan username `yiran00` dan password `abc123`. Login ditolak karena password kurang dari delapan karakter.

3. **Password tanpa angka**

   Menggunakan username `yirannn` dan password `passwordLama`. Login ditolak karena password tidak mengandung angka.

4. **Login berhasil**

   Menggunakan username `zhouyiran2000` dan password `aman12345`. Login berhasil karena username dan password sesuai dengan data pengguna yang tersimpan serta memenuhi ketentuan validasi.

## Cara Menjalankan Program

1. Pastikan Python sudah terpasang pada komputer.

2. Simpan kode program dalam file bernama `main.py`.

3. Buka terminal atau command prompt pada folder tempat file disimpan.

4. Jalankan perintah berikut.

   ```bash
   python main.py
   ```

5. Hasil empat skenario pengujian akan ditampilkan pada terminal.

## Hasil yang Diharapkan

Program menampilkan judul sistem, nomor dan nama setiap skenario pengujian, waktu percobaan login, status, serta keterangan hasilnya.

Tiga skenario pertama ditolak karena username atau password tidak memenuhi ketentuan validasi. Skenario keempat berhasil karena data akun sesuai dengan database.

## Kesimpulan

Program Sistem Keamanan Akun dan Audit Log menerapkan validasi username dan password serta pencatatan hasil percobaan login menggunakan Python. Melalui empat skenario pengujian, program menunjukkan cara menangani input yang tidak valid dan memeriksa kecocokan data akun.

Program ini dapat digunakan sebagai media pembelajaran untuk memahami class, property, setter, regular expression, decorator, dan penanganan kesalahan. Namun, program masih berupa simulasi dasar karena password disimpan dalam bentuk teks biasa dan belum menggunakan mekanisme autentikasi yang aman untuk aplikasi nyata.
