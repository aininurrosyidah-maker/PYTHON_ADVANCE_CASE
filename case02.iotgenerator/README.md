# Sistem Streaming Data Sensor IoT

## 1. Deskripsi Program

Program Sistem Streaming Data Sensor IoT merupakan program Python yang digunakan untuk mensimulasikan proses pemantauan suhu lingkungan. Program menghasilkan data suhu secara acak, kemudian menampilkan setiap data secara bertahap seperti aliran data yang berasal dari sensor IoT. Setiap suhu yang dihasilkan akan diproses untuk menentukan kategorinya, yaitu dingin, normal, atau panas.

Selain menampilkan suhu, program juga mencatat hasil pembacaan untuk menghitung suhu rata-rata, suhu tertinggi, suhu terendah, dan jumlah data pada setiap kategori. Dengan demikian, program ini tidak hanya menampilkan data yang masuk, tetapi juga memberikan ringkasan hasil pemantauan setelah seluruh proses selesai.

## 2. Tujuan Program

Program ini dibuat untuk mempelajari penerapan konsep streaming data menggunakan Python. Melalui program ini, pengguna dapat memahami bagaimana data dihasilkan secara bertahap menggunakan generator, diproses ketika tersedia, dan ditampilkan dengan jeda waktu tertentu.

Program ini juga bertujuan menerapkan penggunaan fungsi, perulangan, percabangan, serta pengolahan data numerik. Data suhu yang dihasilkan digunakan sebagai contoh sederhana untuk menggambarkan proses pemantauan lingkungan, meskipun program belum terhubung langsung dengan perangkat sensor fisik.

## 3. Library yang Digunakan

Program menggunakan dua library, yaitu `random` dan `time`. Library `random` digunakan untuk menghasilkan nilai suhu secara acak melalui fungsi `random.uniform(15.0, 38.0)`. Nilai tersebut berada dalam rentang 15°C hingga 38°C, kemudian dibulatkan menjadi dua angka di belakang koma menggunakan fungsi `round()`.

Sementara itu, library `time` digunakan untuk memberikan jeda selama 0,3 detik menggunakan `time.sleep(0.3)`. Jeda ini membuat setiap pembacaan suhu ditampilkan secara bertahap, sehingga prosesnya menyerupai aliran data sensor yang terus masuk. Kedua library tersebut mendukung proses simulasi tanpa membutuhkan perangkat tambahan.

## 4. Fungsi Generator Suhu

Fungsi `generator_suhu(jumlah_data=15)` bertugas menghasilkan data suhu sesuai dengan jumlah yang ditentukan. Parameter `jumlah_data` memiliki nilai bawaan 15, sehingga fungsi akan menghasilkan 15 data jika dipanggil tanpa memberikan jumlah lain. Pada setiap perulangan, program menghasilkan suhu acak, membulatkannya menjadi dua angka di belakang koma, lalu mengeluarkannya menggunakan perintah `yield`.

Penggunaan `yield` membuat fungsi bekerja sebagai generator. Artinya, nilai suhu dikeluarkan satu per satu ketika diminta, bukan dikumpulkan sekaligus menjadi sebuah list. Dalam program ini, generator menjadi sumber data yang nantinya dibaca dan diproses oleh fungsi utama. Cara tersebut sesuai dengan konsep streaming karena data dapat ditangani secara bertahap.

## 5. Fungsi Kategorisasi Suhu

Fungsi `kategorisasi_suhu(suhu)` digunakan untuk menentukan kategori suhu berdasarkan nilai yang diterima. Proses ini menggunakan percabangan `if-elif-else` untuk memeriksa rentang suhu dan menghasilkan keterangan yang sesuai.

Terdapat tiga kategori yang digunakan. Suhu di bawah 20°C termasuk kategori **Dingin**, suhu mulai dari 20°C sampai dengan 30°C termasuk kategori **Normal**, sedangkan suhu di atas 30°C termasuk kategori **Panas**. Fungsi ini mengembalikan hasil berupa teks yang kemudian ditampilkan pada tabel streaming. Batas kategori tersebut mengikuti aturan yang telah ditentukan dalam kode program.

## 6. Proses Streaming Data Sensor

Fungsi `jalankan_streaming_sensor()` merupakan fungsi utama yang mengatur jalannya simulasi. Pada awal proses, program menetapkan jumlah pembacaan sebanyak 15 data dan membuat generator melalui pemanggilan `generator_suhu(jumlah_data)`. Program juga menyiapkan variabel untuk menghitung total suhu, suhu minimum, suhu maksimum, serta jumlah data pada kategori dingin, normal, dan panas.

Setelah itu, program menampilkan judul dan kepala tabel yang berisi nomor pembacaan, suhu dalam derajat Celsius, kategori, dan status. Data kemudian diambil dari generator menggunakan perulangan `for` dengan bantuan `enumerate()` untuk memberikan nomor urut mulai dari 1.

Setiap suhu yang diperoleh akan diproses oleh fungsi `kategorisasi_suhu()`. Berdasarkan hasil kategorisasi, program menentukan keterangan berupa "Suhu rendah", "Suhu stabil", atau "Suhu tinggi". Selanjutnya, program memperbarui jumlah kategori yang sesuai, menambahkan suhu ke total pembacaan, serta memperbarui nilai suhu minimum dan maksimum. Data kemudian ditampilkan pada tabel sebelum program menunggu selama 0,3 detik untuk melanjutkan pembacaan berikutnya.

Proses ini berulang sampai seluruh 15 data selesai diproses. Dengan alur tersebut, setiap data langsung ditangani ketika dihasilkan, sekaligus digunakan untuk memperbarui ringkasan hasil pemantauan.

## 7. Perhitungan Ringkasan Hasil Pemantauan

Setelah seluruh data selesai diproses, program menghitung suhu rata-rata dengan membagi total suhu dengan jumlah pembacaan. Perhitungan ini menggunakan variabel `total_suhu` dan `jumlah_data`. Suhu terendah dicatat melalui variabel `suhu_min`, sedangkan suhu tertinggi disimpan dalam variabel `suhu_max`. Kedua variabel tersebut diperbarui pada setiap pembacaan menggunakan fungsi `min()` dan `max()`.

Program juga menghitung jumlah data pada setiap kategori menggunakan variabel `jumlah_dingin`, `jumlah_normal`, dan `jumlah_panas`. Setiap kali suhu masuk ke salah satu kategori, nilai penghitung yang sesuai akan bertambah satu. Setelah seluruh proses selesai, program menampilkan semua hasil tersebut dalam bagian ringkasan.

Ringkasan ini membantu pengguna mengetahui gambaran umum data suhu yang dihasilkan tanpa harus menghitungnya secara manual. Jumlah data dari ketiga kategori akan berjumlah 15 apabila semua pembacaan berhasil diselesaikan.

## 8. Keluaran Program

Program menghasilkan dua bagian keluaran utama. Bagian pertama berupa tabel streaming yang menampilkan nomor pembacaan, suhu, kategori, dan keterangan kondisi suhu. Setiap baris ditampilkan secara bertahap dengan jeda waktu 0,3 detik sehingga pengguna dapat mengikuti proses pembacaan data.

Bagian kedua berupa ringkasan hasil pemantauan yang mencakup jumlah pembacaan, suhu rata-rata, suhu terendah, suhu tertinggi, serta jumlah data dalam kategori dingin, normal, dan panas. Karena suhu dihasilkan secara acak, nilai dan jumlah masing-masing kategori dapat berbeda setiap kali program dijalankan. Namun, selama program berjalan normal hingga selesai, jumlah pembacaannya tetap 15 data.

## 9. Cara Menjalankan Program

Untuk menjalankan program, simpan kode Python dalam sebuah file, misalnya `streaming_sensor.py`. Pastikan Python sudah terpasang pada komputer, kemudian buka terminal dan arahkan ke folder tempat file tersebut disimpan.

Jalankan program menggunakan perintah berikut:

```bash
python streaming_sensor.py
```

Setelah perintah dijalankan, program akan menampilkan judul sistem, tabel pembacaan suhu secara bertahap, dan ringkasan hasil pemantauan setelah seluruh data selesai diproses. Program tidak membutuhkan input dari pengguna karena jumlah data dan rentang suhu sudah ditentukan dalam kode.

## 10. Konsep Python yang Digunakan

Program ini menggunakan beberapa konsep Python yang saling mendukung. Fungsi `generator_suhu()` menerapkan generator dengan `yield` untuk menghasilkan data secara bertahap. Fungsi `kategorisasi_suhu()` menggunakan percabangan untuk menentukan kategori berdasarkan nilai suhu, sedangkan perulangan digunakan untuk membaca dan memproses setiap data yang dihasilkan.

Selain itu, fungsi `enumerate()` digunakan untuk memberikan nomor urut pada pembacaan, `round()` untuk membulatkan nilai suhu, serta `min()` dan `max()` untuk memperbarui suhu terendah dan tertinggi. Variabel penghitung digunakan untuk mencatat jumlah data dalam setiap kategori, sedangkan `time.sleep()` memberikan jeda antar pembacaan. Semua konsep tersebut diterapkan untuk mendukung simulasi streaming dan pengolahan data suhu.

## 11. Kesimpulan

Program Sistem Streaming Data Sensor IoT merupakan simulasi sederhana yang menggambarkan bagaimana data suhu dapat dihasilkan, diproses, dan ditampilkan secara bertahap menggunakan Python. Data suhu dibuat secara acak melalui generator, kemudian dikelompokkan ke dalam kategori dingin, normal, atau panas. Selama proses berlangsung, program juga mencatat nilai suhu dan jumlah kategori untuk menghasilkan ringkasan pada akhir pembacaan.

Melalui program ini, konsep generator, perulangan, percabangan, fungsi, dan pengolahan data numerik dapat diterapkan dalam satu contoh sederhana. Meskipun belum menggunakan sensor fisik, program sudah menggambarkan alur dasar pemantauan data yang dapat dikembangkan lebih lanjut.
