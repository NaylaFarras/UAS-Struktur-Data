from data import baca_data, simpan_data  # Mengimpor fungsi untuk membaca dan menyimpan data transaksi
from tambah_transaksi import input_tanggal, input_nominal  # Mengimpor fungsi input tanggal dan nominal
from tampilkan_transaksi import tampilkan_transaksi  # Mengimpor fungsi untuk menampilkan daftar transaksi

# Fungsi untuk mengubah data transaksi yang sudah ada
def edit_transaksi():
    data = baca_data()            # Membaca seluruh data transaksi dari file CSV
    tampilkan_transaksi()        # Menampilkan semua transaksi ke layar agar user bisa melihat nomor transaksi

    if not data:                 # Jika data kosong, maka keluar dari fungsi (tidak ada yang bisa diubah)
        return

    try:
        # Meminta user memasukkan nomor transaksi yang ingin diubah (dikonversi ke indeks list, jadi dikurangi 1)
        idx = int(input("\nNomor yang ingin diubah: ")) - 1

        # Memastikan bahwa indeks yang dimasukkan masih dalam jangkauan jumlah data
        if 0 <= idx < len(data):
            print("\nMasukkan data baru:")  # Memberi tahu user untuk mengisi ulang data baru

            # Mengisi data baru dengan input dari user
            data[idx] = {
                "tanggal"  : input_tanggal(),   # Input tanggal dengan validasi format
                "jenis"    : input("Jenis transaksi (pemasukan/pengeluaran): ").lower(),  # Input jenis transaksi dan ubah jadi huruf kecil
                "kategori" : input("Kategori: "),    # Input kategori transaksi
                "deskripsi": input("Deskripsi: "),   # Input deskripsi transaksi
                "nominal"  : input_nominal()         # Input nominal transaksi (dengan validasi bilangan positif)
            }

            simpan_data(data)  # Menyimpan kembali data yang telah diperbarui ke file CSV
            print("Transaksi berhasil diubah.")  # Memberi notifikasi bahwa proses berhasil
        else:
            print("Nomor tidak valid.")  # Jika nomor yang dimasukkan di luar jangkauan, tampilkan pesan kesalahan

    except ValueError:
        print("Masukkan angka yang valid.")  # Jika input nomor bukan angka (misalnya huruf), tampilkan pesan kesalahan
