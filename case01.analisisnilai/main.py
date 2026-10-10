data_mahasiswa = [
    {
        "nama": "Aria Cahya",
        "nim": "281125001",
        "program_studi": "Teknik Informatika",
        "kelas": "TI-1A",
        "tugas": 89,
        "uts": 86,
        "uas": 78
    },
    {
        "nama": "Tisa Melsa",
        "nim": "281125002",
        "program_studi": "Sastra Inggris",
        "kelas": "SI-3B",
        "tugas": 72,
        "uts": 79,
        "uas": 75
    },
    {
        "nama": "Daffa Reka",
        "nim": "281125003",
        "program_studi": "Sastra Jepang",
        "kelas": "SJ-2A",
        "tugas": 98,
        "uts": 89,
        "uas": 91
    },
    {
        "nama": "Rizky Aditya",
        "nim": "281125004",
        "program_studi": "Pendidikan Matematika",
        "kelas": "PM-1B",
        "tugas": 88,
        "uts": 84,
        "uas": 87
    },
    {
        "nama": "Claresta Reva",
        "nim": "281125005",
        "program_studi": "Hukum",
        "kelas": "HU-3A",
        "tugas": 86,
        "uts": 90,
        "uas": 96
    }
]


# 1. Menghitung nilai akhir
mahasiswa_dengan_nilai = [
    {
        **m,
        "nilai_akhir": round(
            m["tugas"] * 0.30
            + m["uts"] * 0.30
            + m["uas"] * 0.40,
            2
        )
    }
    for m in data_mahasiswa
]


# 2. Memfilter mahasiswa berprestasi
mahasiswa_berprestasi = list(
    filter(
        lambda m: m["nilai_akhir"] > 80,
        mahasiswa_dengan_nilai
    )
)


# 3. Membuat pemeringkatan mahasiswa
ranking = sorted(
    mahasiswa_dengan_nilai,
    key=lambda m: m["nilai_akhir"],
    reverse=True
)


# 4. Fungsi untuk menampilkan tabel nilai
def tampilkan_tabel(judul, daftar, tampilkan_rank=True):
    print(f"\n{judul}")
    print("-" * 90)

    if tampilkan_rank:
        print(
            f"{'Rank':<6}{'Nama':<27}{'NIM':<15}"
            f"{'Tugas':>7}{'UTS':>7}{'UAS':>7}{'Akhir':>9}"
        )
    else:
        print(
            f"{'Nama':<27}{'NIM':<15}"
            f"{'Tugas':>7}{'UTS':>7}{'UAS':>7}{'Akhir':>9}"
        )

    print("-" * 90)

    for nomor, m in enumerate(daftar, start=1):
        if tampilkan_rank:
            print(
                f"{nomor:<6}{m['nama']:<27}{m['nim']:<15}"
                f"{m['tugas']:>7}{m['uts']:>7}"
                f"{m['uas']:>7}{m['nilai_akhir']:>9.2f}"
            )
        else:
            print(
                f"{m['nama']:<27}{m['nim']:<15}"
                f"{m['tugas']:>7}{m['uts']:>7}"
                f"{m['uas']:>7}{m['nilai_akhir']:>9.2f}"
            )


# 5. Fungsi utama program
def main():
    print("Analisis Nilai Mahasiswa")
    print("Bobot: Tugas 30%, UTS 30%, UAS 40%")

    # Menampilkan seluruh nilai mahasiswa
    tampilkan_tabel(
        "Daftar Nilai Mahasiswa",
        mahasiswa_dengan_nilai,
        tampilkan_rank=False
    )

    # Menampilkan mahasiswa berprestasi
    tampilkan_tabel(
        "Mahasiswa Berprestasi (Nilai Akhir > 80)",
        mahasiswa_berprestasi,
        tampilkan_rank=False
    )

    # Menampilkan ranking seluruh mahasiswa
    tampilkan_tabel(
        "Pemeringkatan (Ranking) Mahasiswa",
        ranking
    )

    # Menampilkan mahasiswa terbaik
    terbaik = ranking[0]

    print("\nMahasiswa Terbaik")
    print(f"Nama          : {terbaik['nama']}")
    print(f"NIM           : {terbaik['nim']}")
    print(f"Program Studi : {terbaik['program_studi']}")
    print(f"Kelas         : {terbaik['kelas']}")
    print(f"Nilai Tugas   : {terbaik['tugas']}")
    print(f"Nilai UTS     : {terbaik['uts']}")
    print(f"Nilai UAS     : {terbaik['uas']}")
    print(f"Nilai Akhir   : {terbaik['nilai_akhir']:.2f}")


if __name__ == "__main__":
    main()