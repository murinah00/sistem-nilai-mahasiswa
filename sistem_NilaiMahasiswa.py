# =====================================================
# SISTEM NILAI MAHASISWA
# Mata Kuliah: Pemrograman Berorientasi Objek
# =====================================================

class Mahasiswa:
    """Class untuk menyimpan data identitas mahasiswa"""
    
    # Menghitung jumlah mahasiswa — untuk Class Method
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, jurusan):
        """Konstruktor — otomatis dijalankan saat objek dibuat"""
        # Atribut privat (Encapsulation)
        self._nama = nama
        self._nim = nim
        self._jurusan = jurusan
        Mahasiswa.jumlah_mahasiswa += 1

    # ===================== PROPERTY & SETTER =====================
    @property
    def nama(self):
        """Getter — mengambil nilai nama"""
        return self._nama

    @nama.setter
    def nama(self, nilai_baru):
        """Setter — mengubah nama dengan validasi sederhana"""
        if len(nilai_baru) > 2:
            self._nama = nilai_baru
        else:
            print("Nama terlalu pendek!")

    @property
    def nim(self):
        return self._nim

    @property
    def jurusan(self):
        return self._jurusan

    # ===================== CLASS METHOD =====================
    @classmethod
    def dari_data_kampus(cls, nama, nim):
        """Class Method — buat objek dengan format sederhana"""
        return cls(nama, nim, "Ilmu Komputer")

    @classmethod
    def tampilkan_jumlah(cls):
        print(f"Total Mahasiswa: {cls.jumlah_mahasiswa}")

    # ===================== STATIC METHOD =====================
    @staticmethod
    def konversi_nilai(angka):
        """Static Method — ubah angka nilai ke huruf"""
        if angka >= 85:
            return "A"
        elif angka >= 75:
            return "B"
        elif angka >= 65:
            return "C"
        elif angka >= 55:
            return "D"
        else:
            return "E"

    def tampilkan_info(self):
        """Method biasa — tampilkan data mahasiswa"""
        print(f"Nama    : {self._nama}")
        print(f"NIM     : {self._nim}")
        print(f"Jurusan : {self._jurusan}")


class NilaiAkademik:
    """Class kedua — khusus untuk mengelola data nilai"""

    def __init__(self, mahasiswa, mata_kuliah, nilai_angka):
        """Konstruktor"""
        self._mahasiswa = mahasiswa
        self._mata_kuliah = mata_kuliah
        self._nilai_angka = nilai_angka

    # Property & Setter untuk nilai
    @property
    def nilai_angka(self):
        return self._nilai_angka

    @nilai_angka.setter
    def nilai_angka(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self._nilai_angka = nilai_baru
        else:
            print("Nilai harus antara 0 - 100")

    def tampilkan_nilai(self):
        """Tampilkan lengkap nilai + konversi huruf"""
        print("-" * 40)
        self._mahasiswa.tampilkan_info()
        print(f"Mata Kuliah: {self._mata_kuliah}")
        print(f"Nilai Angka: {self._nilai_angka}")
        huruf = Mahasiswa.konversi_nilai(self._nilai_angka)
        print(f"Nilai Huruf : {huruf}")
        print("-" * 40)


# =====================================================
# PROGRAM UTAMA — Membuat Objek & Menjalankan
# =====================================================

if __name__ == "__main__":
    print("=" * 45)
    print("     ILMU KOMPUTER NILAI MAHASISWA")
    print("=" * 45)

    # 1. Membuat objek dari Class Mahasiswa
    mhs1 = Mahasiswa("Murinah", "3C-KOM", "Ilmu Komputer ")
    mhs2 = Mahasiswa.dari_data_kampus("Melisaa", "3C-KOM")

    # 2. Ubah nama menggunakan SETTER
    mhs2.nama = "Melisa"

    # 3. Tampilkan jumlah mahasiswa menggunakan CLASS METHOD
    Mahasiswa.tampilkan_jumlah()
    print()

    # 4. Buat objek NilaiAkademik
    nilai1 = NilaiAkademik(mhs1, "Pemrograman Berorientasi Objek", 88)
    nilai2 = NilaiAkademik(mhs2, "Pemrograman Berorientasi Objek", 72)

    # 5. Tampilkan hasil
    nilai1.tampilkan_nilai()
    nilai2.tampilkan_nilai()

    # 6. Contoh Static Method langsung
    print("\n Contoh Static Method — Konversi Nilai:")
    print(f"Nilai 90 = {Mahasiswa.konversi_nilai(90)}")
    print(f"Nilai 60 = {Mahasiswa.konversi_nilai(60)}")

    