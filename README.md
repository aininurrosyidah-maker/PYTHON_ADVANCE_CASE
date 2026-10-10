# PythonAdvancedCaseStudy

1.Identitas Mahasiswa

Nama: Aini Nur Rosyidah
NIM: 2595114024
Kelas: Teknik Informatika (1125B)
Mata Kuliah: Python Advanced Topics

2.Deskripsi Proyek

Repository ini berisi pengerjaan tugas mandiri mata kuliah Python Advanced Topics yang terdiri dari tiga studi kasus. Setiap studi kasus memiliki permasalahan yang berbeda dan menggunakan konsep Python lanjutan sesuai dengan kebutuhan program.

Studi kasus pertama membahas pengolahan nilai mahasiswa, mulai dari menghitung nilai akhir sampai menentukan peringkat mahasiswa. Studi kasus kedua membahas pembacaan data suhu sensor IoT secara bertahap agar data dapat diproses tanpa harus menyimpan seluruhnya dalam satu list. Studi kasus ketiga membahas validasi username dan password serta pencatatan aktivitas login.

Setiap studi kasus memiliki file program Python, README khusus untuk menjelaskan cara kerja program, dan gambar hasil eksekusi. Dengan susunan tersebut, kode program dan dokumentasinya lebih mudah dibaca serta diperiksa kembali.

3.Studi Kasus

3.1 Analisis Nilai Mahasiswa

Program ini digunakan untuk mengolah data nilai mahasiswa yang terdiri dari nilai tugas, UTS, dan UAS. Nilai akhir dihitung berdasarkan bobot tugas sebesar 30%, UTS sebesar 30%, dan UAS sebesar 40%.

Setelah nilai akhir diperoleh, program menampilkan seluruh nilai mahasiswa dalam bentuk tabel. Program juga menyaring mahasiswa yang memiliki nilai akhir di atas 80, mengurutkan mahasiswa dari nilai tertinggi hingga terendah, dan menentukan mahasiswa terbaik beserta informasi nilai dan identitasnya.

Dengan adanya program ini, pengolahan nilai menjadi lebih praktis karena perhitungan dan pemeringkatan dilakukan secara otomatis.

Konsep Python yang digunakan:

List Comprehension: Menghitung nilai akhir setiap mahasiswa dengan mengolah data yang tersedia.
Lambda Function: Menentukan nilai akhir sebagai dasar pengurutan mahasiswa.
Filtering: Memilih mahasiswa yang memperoleh nilai akhir di atas 80.
Sorting: Mengurutkan mahasiswa berdasarkan nilai akhir menggunakan fungsi "sorted()".

Folder: "case01.analisisnilai"

3.2 Streaming Data Sensor IoT

Program ini menyimulasikan pembacaan data suhu dari sensor IoT. Data suhu dihasilkan secara bertahap menggunakan generator, kemudian diproses satu per satu. Cara ini digunakan agar program tidak perlu menyimpan seluruh data sekaligus dalam list yang besar.

Setiap data suhu yang diperoleh akan diperiksa dan dikelompokkan ke dalam tiga kategori, yaitu Dingin, Normal, dan Panas. Hasil pembacaan menampilkan nomor data, nilai suhu, kategori, dan status suhu agar mudah diperiksa melalui terminal.

Penggunaan generator membantu program memproses data secara bertahap sehingga penggunaan memori dapat lebih efisien, terutama ketika jumlah data yang diproses semakin banyak.

Konsep Python yang digunakan:

Iterator Pattern: Mengambil dan memproses data secara berurutan.
Generator Function: Menghasilkan data suhu secara bertahap ketika dibutuhkan.
"yield": Mengembalikan nilai dari generator tanpa harus menghasilkan seluruh data sekaligus.
"next()": Mengambil nilai berikutnya dari generator.
Efisiensi Memori: Mengurangi kebutuhan penyimpanan karena data diproses satu per satu.

Folder: "case02.iotgenerator"

3.3 Sistem Keamanan Akun dan Audit Log Login

Program ini digunakan untuk memeriksa format username dan password sebelum proses login dilakukan. Username harus memiliki minimal lima karakter dan hanya terdiri dari huruf serta angka. Password harus memiliki minimal delapan karakter dan mengandung setidaknya satu angka.

Program menggunakan class "User" untuk mengelola data pengguna dan "@property" untuk mengatur akses serta validasi atribut. Selain itu, decorator digunakan untuk mencatat aktivitas login secara otomatis.

Catatan audit berisi waktu percobaan login, nama pengguna, status login, dan alasan penolakan jika login gagal. Program diuji menggunakan beberapa kondisi, seperti username yang tidak sesuai aturan, password yang tidak valid, dan login dengan format yang benar.

Melalui pengujian tersebut, program dapat menunjukkan bagaimana validasi data dan pencatatan aktivitas digunakan dalam simulasi keamanan akun.

Konsep Python yang digunakan:

Regular Expression ("re"): Memeriksa format username dan password berdasarkan aturan yang ditentukan.
Class dan Object: Mengelola data serta perilaku pengguna melalui class "User".
"@property": Mengatur akses dan validasi atribut pengguna.
Decorator: Menambahkan proses pencatatan pada fungsi login tanpa harus menulis ulang fungsi utamanya.
Closure: Mendukung pembuatan fungsi pembungkus yang digunakan dalam decorator.
Audit Logging: Mencatat aktivitas login untuk melihat hasil percobaan dan alasan kegagalan.

Folder: "case03.loginsecurity"

4.Struktur Repository

Repository ini dibagi menjadi satu folder utama dan tiga folder studi kasus. Setiap folder studi kasus berisi file program Python, README khusus, dan gambar hasil eksekusi.

PYTHON_ADVANCE_CASE/
├── README.md
├── case01.analisisnilai/
│   ├── main.py
│   ├── output.case01.png
│   └── README.md
├── case02.iotgenerator/
│   ├── main.py
│   ├── output.case02.png
│   └── README.md
└── case03.loginsecurity/
    ├── main.py
    ├── output.case03.png
    └── README.md

File "README.md" utama menjelaskan gambaran keseluruhan proyek. Sementara itu, README di setiap folder digunakan untuk menjelaskan studi kasus secara lebih khusus, termasuk tujuan program, konsep yang digunakan, dan cara menjalankannya.

File gambar digunakan sebagai bukti hasil eksekusi program. Dengan pembagian tersebut, setiap studi kasus dapat diperiksa secara terpisah tanpa mencampurkan kode dan dokumentasinya.

5.Persyaratan Program

Sebelum menjalankan program, pastikan beberapa hal berikut sudah tersedia:

Python: Digunakan untuk menjalankan seluruh program pada setiap studi kasus.
Visual Studio Code: Digunakan untuk membuka, mengedit, dan mengelola file program.
Terminal: Digunakan untuk menjalankan program dan melihat hasilnya.
File proyek: Pastikan file "main.py" dan file pendukung berada di folder studi kasus masing-masing.

Ketiga studi kasus menggunakan fitur Python yang dijelaskan dalam dokumentasinya. Jika ada perubahan nama file atau struktur folder, sesuaikan perintah dan dokumentasi agar tetap sesuai dengan kondisi proyek.

6.Cara Menjalankan Program

Berikut langkah-langkah untuk menjalankan salah satu studi kasus melalui Visual Studio Code.

1.Buka folder proyek "PYTHON_ADVANCE_CASE" di Visual Studio Code.

2.Pilih folder studi kasus yang ingin dijalankan.

3.Buka menu Terminal → New Terminal.

4.Pastikan terminal berada di folder studi kasus yang dipilih.

5.Ketik perintah berikut untuk menjalankan program:
   python main.py

6.Tekan Enter dan tunggu sampai program selesai dijalankan.

7.Periksa hasil yang muncul di terminal dan pastikan hasilnya sesuai dengan fungsi program.

Jika perintah "python main.py" tidak dapat digunakan pada komputer, coba jalankan "python3 main.py". Pastikan juga nama file yang digunakan benar dan Python sudah terpasang.

7.Bukti Eksekusi Program

Setiap studi kasus dilengkapi dengan screenshot hasil eksekusi program melalui terminal. Screenshot disimpan di folder masing-masing studi kasus agar hasil program dapat dilihat kembali tanpa harus langsung menjalankannya.

Bukti eksekusi membantu menunjukkan bahwa program telah dijalankan dan menghasilkan keluaran. Sebelum dikumpulkan, pastikan gambar terlihat jelas, sesuai dengan program yang dijalankan, dan menggunakan nama file yang sama dengan yang tercantum dalam README.

8.Progres Pengerjaan

Bagian ini digunakan untuk memeriksa kelengkapan tugas sebelum dikumpulkan.

[ ] Case 01 — Analisis Nilai Mahasiswa
[ ] Case 02 — Streaming Data Sensor IoT
[ ] Case 03 — Sistem Keamanan Akun dan Audit Log Login
[ ] README utama sudah dibuat.
[ ] README setiap studi kasus sudah dibuat.
[ ] Screenshot hasil eksekusi setiap program sudah tersedia.
[ ] Repository sudah diperiksa sebelum dikumpulkan.

Setiap bagian dapat ditandai selesai setelah program, dokumentasi, dan screenshot terkait benar-benar tersedia dan sudah diperiksa. Checklist ini membantu memastikan tidak ada bagian tugas yang tertinggal.

## Kesimpulan

Melalui tiga studi kasus ini, saya mempelajari cara mengolah nilai mahasiswa, membaca data suhu sensor secara bertahap, serta memvalidasi username dan password menggunakan Python. Setiap studi kasus memberikan pemahaman tentang penggunaan konsep Python yang berbeda sesuai dengan kebutuhan program.

Selain itu, tugas ini membantu saya memahami penggunaan List Comprehension, Lambda Function, Generator, RegEx, "@property", dan Decorator. Saya juga belajar menyusun file program, membuat dokumentasi README, dan menyimpan hasil eksekusi dalam folder yang teratur.

Dengan adanya tugas ini, saya menjadi lebih memahami cara menerapkan konsep Python lanjutan dalam menyelesaikan permasalahan sederhana.
# PYTHON_ADVANCE_CASE
