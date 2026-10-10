
import random
import time


def generator_suhu(jumlah_data=12):
    """Menghasilkan data suhu secara bertahap."""
    for _ in range(jumlah_data):
        yield round(random.uniform(15.0, 38.0), 2)


def kategorisasi_suhu(suhu):
    """Menentukan kategori suhu."""
    if suhu < 15.0:
        return "Dingin"
    elif suhu <= 25.0:
        return "Normal"
    return "Panas"


def jalankan_streaming_sensor():
    jumlah_data = 12
    total_suhu = 0
    suhu_min = float("inf")
    suhu_max = float("-inf")

    jumlah_dingin = 0
    jumlah_normal = 0
    jumlah_panas = 0

    print("\nSISTEM STREAMING DATA SENSOR IoT")
    print("Pemantauan Suhu Lingkungan")

    for nomor, suhu in enumerate(
        generator_suhu(jumlah_data), start=1
    ):
        kategori = kategorisasi_suhu(suhu)

        if kategori == "Dingin":
            jumlah_dingin += 1
            status = "Suhu rendah"
        elif kategori == "Normal":
            jumlah_normal += 1
            status = "Suhu stabil"
        else:
            jumlah_panas += 1
            status = "Suhu tinggi"

        total_suhu += suhu
        suhu_min = min(suhu_min, suhu)
        suhu_max = max(suhu_max, suhu)

        print(f"\nData ke-{nomor}")
        print(f"Suhu     : {suhu:.2f} °C")
        print(f"Kategori : {kategori}")
        print(f"Status   : {status}")

        time.sleep(0.3)

    rata_rata = total_suhu / jumlah_data

    print("\nRINGKASAN PEMANTAUAN")
    print(f"Total data     : {jumlah_data}")
    print(f"Suhu rata-rata : {rata_rata:.2f} °C")
    print(f"Suhu terendah  : {suhu_min:.2f} °C")
    print(f"Suhu tertinggi : {suhu_max:.2f} °C")
    print(f"Dingin         : {jumlah_dingin} data")
    print(f"Normal         : {jumlah_normal} data")
    print(f"Panas          : {jumlah_panas} data")
    print("\nStreaming sensor selesai.")


if __name__ == "__main__":
    jalankan_streaming_sensor()