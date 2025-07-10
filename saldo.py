# === saldo.py ===
from data import baca_data  # Mengimpor fungsi untuk membaca data transaksi dari file CSV

def cek_saldo():
    data = baca_data()  # Baca semua transaksi dari file

    # Hitung total pemasukan: jumlah semua nominal dengan jenis 'pemasukan'
    pemasukan = sum(d['nominal'] for d in data if d['jenis'] == 'pemasukan')

    # Hitung total pengeluaran: jumlah semua nominal dengan jenis 'pengeluaran'
    pengeluaran = sum(d['nominal'] for d in data if d['jenis'] == 'pengeluaran')

    # Hitung saldo akhir (pemasukan - pengeluaran)
    saldo = pemasukan - pengeluaran

    # Tampilkan saldo ke layar dalam format angka rupiah
    print(f"Rp. {saldo:,}\n")
