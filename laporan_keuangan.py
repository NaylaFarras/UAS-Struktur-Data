from data import baca_data            # Import fungsi baca data transaksi dari file CSV
from collections import defaultdict   # Import defaultdict untuk inisialisasi nilai otomatis ke 0
from saldo import cek_saldo           # Import fungsi untuk menampilkan saldo terkini

def laporan_keseluruhan():
    """
    Fungsi untuk:
    - Menghitung total pemasukan & pengeluaran per bulan dan per tahun
    - Menampilkan laporan tabel bulanan & tahunan
    - Menampilkan saldo akhir
    """

    # 1) Baca semua data transaksi
    data = baca_data()
    if not data:
        print("Belum ada data.")  # Jika data kosong, beri pesan dan keluar
        return

    # 2) Buat tempat penyimpanan total pemasukan dan pengeluaran
    bulanan_in  = defaultdict(int)   # Total pemasukan per bulan
    bulanan_out = defaultdict(int)   # Total pengeluaran per bulan
    tahunan_in  = defaultdict(int)   # Total pemasukan per tahun
    tahunan_out = defaultdict(int)   # Total pengeluaran per tahun

    # 3) Proses setiap transaksi
    for d in data:
        tahun, bulan, *_ = d["tanggal"].split("-")  # Ambil tahun dan bulan dari tanggal

        if d["jenis"] == "pemasukan":
            bulanan_in[f"{tahun}-{bulan}"] += d["nominal"]
            tahunan_in[tahun]              += d["nominal"]
        elif d["jenis"] == "pengeluaran":
            bulanan_out[f"{tahun}-{bulan}"] += d["nominal"]
            tahunan_out[tahun]              += d["nominal"]

    # 4) Tampilkan laporan bulanan
    print("\nLaporan Bulanan:")
    print(f"{'Bulan':<10} | {'Pemasukan':>12} | {'Pengeluaran':>13}")
    print("-" * 42)

    semua_bulan = sorted(set(bulanan_in) | set(bulanan_out))  # Gabungan bulan yang ada
    for bln in semua_bulan:
        masuk  = bulanan_in.get(bln, 0)   # Jika tidak ada, tampilkan 0
        keluar = bulanan_out.get(bln, 0)
        print(f"{bln:<10} | Rp{masuk:>10,} | Rp{keluar:>11,}")

    # 5) Tampilkan laporan tahunan
    print("\nLaporan Tahunan:")
    print(f"{'Tahun':<6} | {'Pemasukan':>12} | {'Pengeluaran':>13}")
    print("-" * 42)

    semua_tahun = sorted(set(tahunan_in) | set(tahunan_out))  # Gabungan tahun yang ada
    for thn in semua_tahun:
        masuk  = tahunan_in.get(thn, 0)
        keluar = tahunan_out.get(thn, 0)
        print(f"{thn:<6} | Rp{masuk:>10,} | Rp{keluar:>11,}")

    # 6) Tampilkan saldo akhir
    print("\nSaldo Akhir:")
    cek_saldo()  # Panggil fungsi untuk menampilkan saldo terakhir (pemasukan - pengeluaran)
