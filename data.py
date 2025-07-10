# === data.py ===
import csv  # Modul untuk membaca dan menulis file CSV

FILENAME = 'keuangan_bersih.csv' # Nama file CSV yang digunakan untuk menyimpan data transaksi

# Fungsi untuk membaca semua data transaksi dari file CSV
def baca_data():
    data = []  # List kosong untuk menampung hasil pembacaan data
    try:
        # Buka file dalam mode baca ('r') dengan encoding UTF-8
        with open(FILENAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Membaca file sebagai list of dictionary
            for row in reader:
                row['nominal'] = int(row['nominal'])  # Konversi nominal dari string ke integer
                data.append(row)  # Tambahkan baris yang sudah dikonversi ke list data
    except FileNotFoundError:
        # Jika file tidak ditemukan, abaikan error dan kembalikan list kosong
        pass
    return data  # Kembalikan list data transaksi

# Fungsi untuk menyimpan seluruh data ke file CSV (menimpa file sebelumnya)
def simpan_data(data):
    # Buka file dalam mode tulis ('w'), otomatis menimpa isi file lama
    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        # Tentukan nama kolom yang digunakan di CSV
        fieldnames = ['tanggal', 'jenis', 'kategori', 'deskripsi', 'nominal']
        writer = csv.DictWriter(file, fieldnames=fieldnames)  # Buat writer untuk dictionary
        writer.writeheader()  # Tulis header kolom ke file
        for d in data:
            writer.writerow(d)  # Tulis setiap transaksi ke file

# Fungsi untuk menambahkan satu data transaksi baru ke file CSV (tanpa menghapus data lama)
def tambah_data_baru(data_baru):
    # Buka file dalam mode append ('a') agar data ditambahkan di akhir file
    with open(FILENAME, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['tanggal', 'jenis', 'kategori', 'deskripsi', 'nominal']
        writer = csv.DictWriter(file, fieldnames=fieldnames)  # Buat writer untuk dictionary
        writer.writerow(data_baru)  # Tulis data transaksi baru ke baris berikutnya
