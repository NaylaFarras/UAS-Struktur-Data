from data import baca_data  # Mengimpor fungsi baca_data dari file data.py

# Fungsi untuk menampilkan seluruh transaksi yang telah tersimpan
def tampilkan_transaksi():
    data = baca_data()  # Membaca data transaksi dari file (CSV) dan simpan ke variabel 'data'

    # Jika data kosong (belum ada transaksi)
    if not data:
        print("Belum ada transaksi.")  # Tampilkan pesan bahwa tidak ada data
        return                         # Keluar dari fungsi ini

    # Menampilkan daftar transaksi satu per satu
    print("\nDaftar Transaksi:")
    for i, d in enumerate(data, 1):  # Perulangan dengan nomor mulai dari 1
        # Tampilkan informasi transaksi dengan format rapi
        print(f"{i}. {d['tanggal']} | {d['jenis']} | {d['kategori']} | "f"{d['deskripsi']} | Rp{d['nominal']:,}")
