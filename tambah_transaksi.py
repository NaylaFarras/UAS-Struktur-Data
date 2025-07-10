from data import baca_data, simpan_data, tambah_data_baru  # Mengimpor fungsi bantu dari file data.py

# Fungsi untuk meminta input tanggal dari pengguna dengan format YYYY-MM-DD
def input_tanggal(prompt="Tanggal (YYYY-MM-DD): "):
    while True:  # Ulangi terus sampai input yang diberikan benar
        t = input(prompt).strip()  # Mengambil input dari pengguna dan menghapus spasi di awal/akhir
        p = t.split("-")           # Memisahkan input berdasarkan tanda "-"
        
        # Memastikan input terdiri dari 3 bagian: tahun, bulan, dan tanggal
        # Setiap bagian harus angka dan panjangnya sesuai: tahun 4 digit, bulan dan tanggal 2 digit
        if len(p) == 3 and all(s.isdigit() for s in p) \
        and len(p[0]) == 4 and len(p[1]) == 2 and len(p[2]) == 2:
            return t  # Jika format benar, kembalikan input
        print("Format salah. Contoh yang benar: 2025-06-28")

# Fungsi untuk meminta input nominal (jumlah uang) dari pengguna
def input_nominal():
    while True:  # Ulangi terus sampai pengguna memasukkan angka yang benar
        try:  # Coba ubah input menjadi integer
            n = int(input("Nominal: "))  # Mengambil input dan mengubahnya ke bilangan bulat
            if n >= 0:  # Pastikan nominal tidak negatif
                return n  # Kembalikan nilai jika valid
            print("Nominal tidak boleh negatif.")  # Tampilkan pesan jika angka negatif
        except ValueError:
            # Jika input tidak bisa diubah ke integer (misalnya huruf), tangkap error-nya
            print("Masukkan angka yang benar.")  # Tampilkan pesan kesalahan

# Fungsi utama untuk menambahkan data transaksi baru
def tambah_transaksi():
    # Mengumpulkan semua data transaksi dari pengguna
    row = {
        "tanggal"   : input_tanggal(),  # Meminta input tanggal
        "jenis"     : input("Jenis transaksi (pemasukan/pengeluaran): ").lower(),  # Input jenis, ubah jadi huruf kecil
        "kategori"  : input("Kategori: "),        # Meminta input kategori transaksi
        "deskripsi" : input("Deskripsi: "),       # Meminta input deskripsi tambahan
        "nominal"   : input_nominal()             # Meminta input jumlah nominal
    }

    # Menyimpan data transaksi ke file melalui fungsi bantu
    tambah_data_baru(row)

    # Menampilkan pesan bahwa data berhasil disimpan
    print("Transaksi berhasil disimpan.\n")
