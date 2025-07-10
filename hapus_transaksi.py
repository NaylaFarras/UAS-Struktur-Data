from data import baca_data, simpan_data             # Impor fungsi untuk membaca dan menyimpan data
from tampilkan_transaksi import tampilkan_transaksi # Impor fungsi untuk menampilkan transaksi

# Fungsi untuk menghapus salah satu transaksi berdasarkan nomor
def hapus_transaksi():
    data = baca_data()           # Membaca data transaksi dari file CSV ke dalam list
    tampilkan_transaksi()       # Menampilkan semua transaksi ke layar

    if not data:                # Jika data kosong, langsung keluar dari fungsi
        return

    try:
        # Minta input nomor transaksi yang ingin dihapus
        idx = int(input("\nNomor yang dihapus: ")) - 1  # Dikurangi 1 agar sesuai dengan indeks list (mulai dari 0)

        if 0 <= idx < len(data):   # Cek apakah indeks valid (dalam jangkauan data)
            data.pop(idx)          # Hapus transaksi dari list
            simpan_data(data)      # Simpan kembali list yang sudah diperbarui ke file
            print("Transaksi terhapus.")  # Tampilkan pesan sukses
        else:
            print("Nomor tidak valid.")     # Jika nomor di luar jangkauan, tampilkan pesan
    except ValueError:
        print("Masukkan angka yang valid.") # Jika input bukan angka, tampilkan pesan kesalahan
