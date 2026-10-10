# Analisis Nilai Mahasiswa Menggunakan Python

## 1. Deskripsi Program

Program Analisis Nilai Mahasiswa merupakan program berbasis Python yang digunakan untuk mengolah dan menganalisis nilai mahasiswa secara otomatis. Program ini memiliki beberapa fungsi utama, yaitu menghitung nilai akhir berdasarkan bobot penilaian, memfilter mahasiswa berprestasi, menyusun pemeringkatan berdasarkan nilai akhir, dan menampilkan informasi mahasiswa terbaik. Hasil pengolahan ditampilkan dalam bentuk tabel teks melalui terminal agar informasi nilai mahasiswa lebih mudah dibaca dan dibandingkan.

## 2. Struktur Data Mahasiswa

Data mahasiswa disimpan dalam variabel `data_mahasiswa` menggunakan struktur data list yang berisi dictionary. Setiap dictionary memuat tujuh atribut, yaitu `nama`, `nim`, `program_studi`, `kelas`, `tugas`, `uts`, dan `uas`. Atribut tersebut digunakan untuk menyimpan identitas mahasiswa, informasi akademik, serta nilai dari setiap komponen penilaian.

Program ini menggunakan lima data mahasiswa, yaitu Aria Cahya, Tisa Melsa, Daffa Reka, Rizky Aditya, dan Claresta Reva. Data tersebut menjadi sumber utama dalam seluruh proses pengolahan nilai, mulai dari perhitungan nilai akhir hingga penentuan mahasiswa dengan nilai tertinggi.

## 3. Perhitungan Nilai Akhir

Perhitungan nilai akhir dilakukan dengan membuat variabel `mahasiswa_dengan_nilai` menggunakan list comprehension. Program memproses setiap data mahasiswa, menyalin seluruh atribut yang tersedia menggunakan operator unpacking dictionary `**m`, kemudian menambahkan atribut baru bernama `nilai_akhir`. Dengan demikian, data hasil pengolahan berisi informasi awal mahasiswa beserta nilai akhir yang telah dihitung.

Rumus perhitungan nilai akhir yang digunakan adalah:

Nilai Akhir = (Tugas × 30%) + (UTS × 30%) + (UAS × 40%)

Nilai tugas memiliki bobot 30%, nilai UTS sebesar 30%, dan nilai UAS sebesar 40%. Hasil perhitungan dibulatkan menjadi dua angka di belakang koma menggunakan fungsi `round()`. Nilai akhir tersebut kemudian digunakan sebagai dasar untuk menyaring mahasiswa berprestasi, menyusun ranking, dan menentukan mahasiswa terbaik.

## 4. Memfilter Mahasiswa Berprestasi

Program menggunakan fungsi `filter()` yang dikombinasikan dengan `lambda` untuk memilih mahasiswa yang memiliki nilai akhir lebih dari 80. Kondisi penyaringan ditulis sebagai `lambda m: m["nilai_akhir"] > 80`. Artinya, hanya mahasiswa yang nilai akhirnya lebih besar dari 80 yang dimasukkan ke dalam kategori mahasiswa berprestasi.

Hasil penyaringan disimpan dalam variabel `mahasiswa_berprestasi` dan dikonversi menjadi list menggunakan fungsi `list()`. Data tersebut kemudian ditampilkan dalam tabel khusus sehingga pengguna dapat mengetahui mahasiswa yang memenuhi kriteria berprestasi berdasarkan hasil perhitungan nilai akhir.

## 5. Pemeringkatan Mahasiswa

Pemeringkatan mahasiswa dilakukan menggunakan fungsi `sorted()` terhadap data dalam variabel `mahasiswa_dengan_nilai`. Parameter `key=lambda m: m["nilai_akhir"]` menentukan bahwa pengurutan didasarkan pada nilai akhir mahasiswa, sedangkan `reverse=True` mengatur urutan dari nilai tertinggi ke nilai terendah. Hasil pengurutan disimpan dalam variabel `ranking`.

Proses pemeringkatan mencakup seluruh mahasiswa, bukan hanya mahasiswa berprestasi. Mahasiswa dengan nilai akhir tertinggi akan berada pada urutan pertama, sedangkan mahasiswa dengan nilai akhir terendah berada pada urutan terakhir. Data ranking ini juga digunakan untuk menentukan mahasiswa terbaik secara otomatis.

## 6. Fungsi Menampilkan Tabel

Fungsi `tampilkan_tabel(judul, daftar, tampilkan_rank=True)` digunakan untuk menampilkan data mahasiswa dalam bentuk tabel teks. Parameter `judul` menentukan judul tabel, `daftar` berisi data yang akan ditampilkan, dan `tampilkan_rank` menentukan apakah kolom ranking perlu disertakan. Nilai bawaan parameter `tampilkan_rank` adalah `True`.

Di dalam fungsi tersebut, percabangan `if-else` digunakan untuk menentukan format tabel dengan atau tanpa kolom ranking. Fungsi `enumerate()` menghasilkan nomor urut yang dimulai dari 1, sedangkan f-string dengan pengaturan lebar kolom digunakan untuk merapikan tampilan nama, NIM, nilai tugas, UTS, UAS, dan nilai akhir. Fungsi ini digunakan kembali untuk menampilkan daftar nilai mahasiswa, mahasiswa berprestasi, serta pemeringkatan sehingga kode lebih terstruktur dan tidak perlu mengulang penulisan format tabel.

## 7. Fungsi Utama Program

Fungsi `main()` mengatur urutan pelaksanaan program. Pertama, program menampilkan judul analisis nilai mahasiswa dan informasi bobot penilaian. Selanjutnya, program menampilkan tabel seluruh nilai mahasiswa, tabel mahasiswa berprestasi dengan nilai akhir lebih dari 80, serta tabel pemeringkatan dari nilai tertinggi hingga terendah.

Setelah seluruh tabel ditampilkan, program menentukan mahasiswa terbaik menggunakan perintah `terbaik = ranking[0]`. Karena data dalam `ranking` telah diurutkan dari nilai tertinggi ke terendah, elemen pertama merupakan mahasiswa dengan nilai akhir tertinggi. Program kemudian menampilkan nama, NIM, program studi, kelas, nilai tugas, nilai UTS, nilai UAS, dan nilai akhir mahasiswa tersebut.

Pada bagian akhir kode, pernyataan `if __name__ == "__main__":` digunakan untuk menjalankan fungsi `main()` ketika file Python dieksekusi secara langsung.

## 8. Konsep Python yang Digunakan

Program ini menerapkan beberapa konsep Python, antara lain list dan dictionary untuk menyimpan data, list comprehension untuk membentuk data baru, serta operator unpacking dictionary `**m` untuk menyalin atribut mahasiswa. Fungsi `round()` digunakan untuk membulatkan nilai akhir, sedangkan `filter()` dan `lambda` digunakan untuk menyaring mahasiswa berdasarkan kriteria tertentu.

Selain itu, fungsi `sorted()` digunakan untuk menyusun ranking, `enumerate()` untuk menghasilkan nomor urut, dan f-string untuk mengatur tampilan tabel. Program juga memanfaatkan perulangan `for`, percabangan `if-else`, serta fungsi buatan sendiri untuk memisahkan proses pengolahan dan penyajian data.

## 9. Keluaran Program

Program menghasilkan empat keluaran utama melalui terminal. Keluaran pertama adalah tabel seluruh nilai mahasiswa yang menampilkan nilai tugas, UTS, UAS, dan nilai akhir. Keluaran kedua adalah tabel mahasiswa berprestasi yang memiliki nilai akhir lebih dari 80. Keluaran ketiga adalah tabel ranking seluruh mahasiswa yang diurutkan berdasarkan nilai akhir dari tertinggi ke terendah. Keluaran keempat adalah informasi lengkap mahasiswa terbaik yang menempati posisi pertama dalam ranking.

Seluruh keluaran tersebut diperoleh dari lima data mahasiswa yang telah ditentukan dalam kode dan dihitung menggunakan bobot penilaian yang sama. Program tidak menggunakan input dari pengguna karena seluruh data mahasiswa sudah tersedia pada variabel `data_mahasiswa`.

## 10. Kesimpulan

Program Analisis Nilai Mahasiswa merupakan penerapan bahasa pemrograman Python untuk mengolah data nilai secara sistematis. Program dapat menghitung nilai akhir berdasarkan bobot tugas, UTS, dan UAS, menentukan mahasiswa berprestasi, menyusun pemeringkatan, serta menampilkan informasi mahasiswa dengan nilai tertinggi. Penggunaan struktur data, fungsi bawaan Python, dan fungsi buatan sendiri membantu membuat proses pengolahan nilai lebih terorganisasi dan hasilnya lebih mudah dipahami.
