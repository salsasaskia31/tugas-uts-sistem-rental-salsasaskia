class Kendaraan:
    def __init__(self, nama, harga_sewa, stok):
        self.nama = nama
        self.__harga_sewa = harga_sewa
        self.stok = stok

    # Property
    @property
    def harga_sewa(self):
        return self.__harga_sewa

    # Setter
    @harga_sewa.setter
    def harga_sewa(self, nilai):
        if nilai >= 0:
            self.__harga_sewa = nilai
        else:
            print("Harga tidak boleh negatif!")

    # Static Method
    @staticmethod
    def rupiah(angka):
        return "Rp" + format(angka, ",").replace(",", ".")


class Rental:
    def __init__(self, nama_rental):
        self.nama_rental = nama_rental
        self.daftar_kendaraan = [
            Kendaraan("Motor Beat", 75000, 5),
            Kendaraan("Motor Vario", 100000, 4),
            Kendaraan("Motor NMAX", 150000, 3),
            Kendaraan("Mobil Avanza", 350000, 2),
            Kendaraan("Mobil Xenia", 350000, 2)
        ]
        self.penyewaan = []

    # Class Method
    @classmethod
    def buat_rental(cls):
        return cls("RENTAL KENDARAAN")

    # Menampilkan kendaraan
    def tampilkan_kendaraan(self):
        print("\n===== DAFTAR KENDARAAN =====")

        for i, kendaraan in enumerate(self.daftar_kendaraan, 1):
            print("\nNomor:", i)
            print("Nama:", kendaraan.nama)
            print("Harga sewa per hari:",
                  Kendaraan.rupiah(kendaraan.harga_sewa))
            print("Stok:", kendaraan.stok)

    # Menyewa kendaraan
    def sewa_kendaraan(self):
        self.tampilkan_kendaraan()

        try:
            nomor = int(input("\nPilih nomor kendaraan: "))

            if nomor < 1 or nomor > len(self.daftar_kendaraan):
                print("Pilihan tidak tersedia!")
                return

            kendaraan = self.daftar_kendaraan[nomor - 1]

            if kendaraan.stok <= 0:
                print("Kendaraan sedang tidak tersedia!")
                return

            nama_penyewa = input("Nama penyewa: ")
            lama = int(input("Lama sewa (hari): "))

            if lama <= 0:
                print("Lama sewa harus lebih dari 0!")
                return

            total = kendaraan.harga_sewa * lama

            kendaraan.stok -= 1

            self.penyewaan.append(
                (nama_penyewa, kendaraan, lama, total)
            )

            print("\nPenyewaan berhasil!")
            print("Nama penyewa:", nama_penyewa)
            print("Kendaraan:", kendaraan.nama)
            print("Lama sewa:", lama, "hari")
            print("Total biaya:", Kendaraan.rupiah(total))

        except ValueError:
            print("Masukkan angka dengan benar!")

    # Melihat data penyewaan
    def tampilkan_penyewaan(self):
        print("\n===== DATA PENYEWAAN =====")

        if not self.penyewaan:
            print("Belum ada data penyewaan!")
            return

        for i, data in enumerate(self.penyewaan, 1):
            nama, kendaraan, lama, total = data

            print("\nPenyewaan:", i)
            print("Nama:", nama)
            print("Kendaraan:", kendaraan.nama)
            print("Lama sewa:", lama, "hari")
            print("Total:", Kendaraan.rupiah(total))

    # Mengembalikan kendaraan
    def kembalikan_kendaraan(self):
        self.tampilkan_penyewaan()

        if not self.penyewaan:
            return

        try:
            nomor = int(input("\nPilih nomor penyewaan: "))

            if nomor < 1 or nomor > len(self.penyewaan):
                print("Data tidak ditemukan!")
                return

            data = self.penyewaan.pop(nomor - 1)
            nama, kendaraan, lama, total = data

            kendaraan.stok += 1

            print("Kendaraan", kendaraan.nama,
                  "berhasil dikembalikan!")

        except ValueError:
            print("Masukkan angka dengan benar!")


# Membuat object
rental = Rental.buat_rental()

# Menu utama
while True:
    print("\n===== SISTEM RENTAL =====")
    print("1. Lihat Kendaraan")
    print("2. Sewa Kendaraan")
    print("3. Data Penyewaan")
    print("4. Pengembalian Kendaraan")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        rental.tampilkan_kendaraan()

    elif pilihan == "2":
        rental.sewa_kendaraan()

    elif pilihan == "3":
        rental.tampilkan_penyewaan()

    elif pilihan == "4":
        rental.kembalikan_kendaraan()

    elif pilihan == "5":
        print("Terima kasih sudah menggunakan sistem rental!")
        break

    else:
        print("Pilihan tidak tersedia!")