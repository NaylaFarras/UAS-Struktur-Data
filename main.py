# === main.py ===

# Import fungsi-fungsi dari modul lain
from tambah_transaksi import tambah_transaksi         # Fungsi untuk menambahkan transaksi baru
from tampilkan_transaksi import tampilkan_transaksi   # Fungsi untuk menampilkan seluruh riwayat transaksi
from hapus_transaksi import hapus_transaksi           # Fungsi untuk menghapus transaksi berdasarkan nomor
from edit_transaksi import edit_transaksi             # Fungsi untuk mengubah/edit data transaksi
from laporan_keuangan import laporan_keseluruhan      # Fungsi untuk menampilkan laporan keuangan per bulan & tahun
from saldo import cek_saldo                           # Fungsi untuk menghitung dan menampilkan saldo akhir

# Fungsi utama yang menampilkan menu CLI dan memproses pilihan pengguna
def menu():
    while True:
        # Menampilkan menu utama
        print("=== SISTEM MANAJEMEN KEUANGAN PRIBADI BERBASIS PYTHON ===")
        print("1. Tambah Transaksi")
        print("2. Lihat Riwayat Transaksi")
        print("3. Hapus Transaksi")
        print("4. Edit Transaksi")
        print("5. Laporan Keuangan Bulanan dan Tahunan")
        print("6. Cek Saldo")
        print("7. Keluar")

        # Menerima input pilihan dari pengguna
        pilih = input("Pilih menu (1-7): ")

        # Menjalankan fungsi sesuai pilihan pengguna
        if pilih == '1':
            tambah_transaksi()               # Menjalankan fitur tambah transaksi
        elif pilih == '2':
            tampilkan_transaksi()            # Menjalankan fitur lihat transaksi
        elif pilih == '3':
            hapus_transaksi()                # Menjalankan fitur hapus transaksi
        elif pilih == '4':
            edit_transaksi()                 # Menjalankan fitur edit transaksi
        elif pilih == '5':
            laporan_keseluruhan()            # Menjalankan fitur laporan bulanan dan tahunan
        elif pilih == '6':
            cek_saldo()                      # Menjalankan fitur cek saldo akhir
        elif pilih == '7':
            print("Terima kasih telah menggunakan aplikasi ini.")  # Pesan keluar
            break                             # Keluar dari program (loop berhenti)
        else:
            print("Pilihan tidak valid.")     # Pesan jika input tidak dikenali

# Titik awal program: hanya dijalankan jika file ini langsung dieksekusi
if __name__ == "__main__":
    menu()  # Memanggil fungsi menu utama
