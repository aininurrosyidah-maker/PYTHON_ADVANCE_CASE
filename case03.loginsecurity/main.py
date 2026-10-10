
import re
import datetime
from functools import wraps


class User:
    """Menyimpan dan memvalidasi data pengguna."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not re.fullmatch(
            r"[a-zA-Z0-9]{5,}", value
        ):
            raise ValueError(
                "Username minimal 5 karakter dan hanya huruf atau angka."
            )
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str) or len(value) < 8:
            raise ValueError("Password minimal 8 karakter.")

        if not re.search(r"\d", value):
            raise ValueError("Password harus mengandung angka.")

        self._password = value


def audit_log(func):
    """Mencatat hasil percobaan login."""

    @wraps(func)
    def wrapper(username, password, database_users):
        waktu = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        status = "DITOLAK"
        alasan = ""

        try:
            user = User(username, password)

            if user.username not in database_users:
                alasan = "Username tidak ditemukan."
            elif database_users[user.username] != user.password:
                alasan = "Password tidak sesuai."
            else:
                status = "BERHASIL"
                func(username, password, database_users)

        except ValueError as error:
            alasan = str(error)

        print(f"\nPengujian login: {username}")
        print(f"Waktu      : {waktu}")
        print(f"Status     : {status}")
        print(
            f"Keterangan : {alasan if alasan else 'Login berhasil.'}"
        )

        return status == "BERHASIL"

    return wrapper


@audit_log
def login_system(username, password, database_users):
    """Menjalankan proses login."""
    return True


def main():
    database_users = {
        "admin123": "rahasia2026",
        "budiUtomo": "password789",
        "zhouyiran2000": "aman12345"
    }

    skenario = [
        ("Username tidak valid", "yiran!", "securePass1"),
        ("Password terlalu pendek", "yiran00", "abc123"),
        ("Password tanpa angka", "yirannn", "passwordLama"),
        ("Login berhasil", "zhouyiran2000", "aman12345")
    ]

    print()
    print("SISTEM KEAMANAN AKUN DAN AUDIT LOG")

    for nomor, (judul, username, password) in enumerate(
        skenario, start=1
    ):
        print(f"\n{nomor}. {judul}")
        login_system(username, password, database_users)

    print("\nPengujian selesai.")


if __name__ == "__main__":
    main()