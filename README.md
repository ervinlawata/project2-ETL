# project2-ETL
## Latar Belakang
Sebuah perusahaan retail ingin menganalisis performa penjualan produk mereka dari berbagai cabang. Data penjualan berasal dari beberapa sumber, termasuk file CSV, database MySQL, dan API eksternal. Perusahaan ingin mengkonsolidasikan data ini ke dalam data warehouse untuk analisis lebih lanjut.
## Tujuan
- Menggunakan proses ETL (Extract, Transform, Load) untuk mengumpulkan data dari berbagai sumber.
- Membersihkan dan mengubah data agar konsisten.
- Memasukkan data yang sudah diproses ke dalam database untuk analisis lebih lanjut.
## Dataset
Sumber data terdiri dari:
- File CSV: Berisi transaksi harian dari toko fisik.
- Database PostgreSQL: Menyimpan Transaksi Harian.
## Arsitektur ETL
- Extract: Mengambil data dari CSV, MySQL, dan API.
- Transform:
  - Membersihkan data (menghapus duplikat, menangani nilai kosong).
  - Mengonversi mata uang transaksi menggunakan API kurs.
  - Menormalisasi data produk dan transaksi.
- Load: Memasukkan data yang telah dibersihkan ke dalam PostgreSQL sebagai data warehouse.
## Implementasi ETL
Menggunakan Python dengan library seperti polars, SQLAlchemy, dan psycopg2 untuk mengelola proses ETL.
## 7.Kesimpulan
Proses ETL ini berhasil mengotomatisasi pengumpulan dan pembersihan data dari berbagai sumber, memastikan data siap digunakan untuk analisis bisnis yang lebih dalam.

Studi kasus ini bisa dimasukkan ke dalam portofolio sebagai contoh implementasi nyata dari keterampilan ETL untuk Data Engineer.







