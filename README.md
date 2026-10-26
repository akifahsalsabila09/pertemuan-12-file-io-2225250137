
# Pertemuan 12 - File I/O dan Error Handling

**Nama:** AKIFAH SALSABILA  
**NIM:** 2225250137  
**Kelas:** 3F

## Tujuan

Mempelajari cara membaca, menulis, dan mengolah data dari file menggunakan Python serta menerapkan penanganan error agar program dapat berjalan dengan baik.

## Format File Input

File input yang digunakan adalah `data/nilai.txt` dengan format data berupa NIM dan nilai yang dipisahkan oleh tanda koma.

Contoh isi file:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Program membaca data dari file tersebut, memeriksa validitas nilai, dan melewati baris yang tidak valid.

## Cara Menjalankan Program

Program dijalankan melalui terminal dari folder utama proyek menggunakan perintah berikut:

```bash
python tugas/rekap_nilai_file.py
```

Program membaca data dari `data/nilai.txt`, menghitung statistik nilai yang valid, kemudian menyimpan hasil rekap ke dalam file `data/hasil_rekap.txt`.

## Error Handling

Program menerapkan penanganan error sebagai berikut:

1. **FileNotFoundError**, digunakan untuk menangani kondisi ketika file input tidak ditemukan.
2. **ValueError**, digunakan untuk menangani kesalahan pemrosesan data, seperti nilai yang bukan angka atau format baris yang tidak sesuai.

Dengan penanganan error tersebut, baris yang tidak valid dapat dilewati sehingga data valid lainnya tetap dapat diproses.

## Hasil Pengujian

| No. | Kasus Pengujian | Hasil yang Diharapkan | Hasil |
|---|---|---|---|
| 1 | Data normal | Data valid berhasil diproses dan statistik nilai dihitung. | Berhasil, 5 data valid diproses. |
| 2 | File tidak ditemukan | Program menampilkan pesan bahwa file tidak ditemukan tanpa menghentikan program secara tidak terkendali. | Pesan file tidak ditemukan ditampilkan. |
| 3 | Nilai tidak valid | Baris dengan nilai bukan angka dilewati dan data valid lainnya tetap diproses. | Baris `A004,abc` dilewati. |
| 4 | Baris kosong | Baris kosong dilewati dan tidak dihitung sebagai data. | Baris kosong dilewati. |
| 5 | Perhitungan statistik | Program menghitung rata-rata, nilai minimum, nilai maksimum, dan jumlah peserta yang lulus. | Rata-rata 83.40, minimum 74.00, maksimum 92.00, dan jumlah lulus 5. |

## Refleksi

Melalui praktikum ini, saya mempelajari cara membaca dan menulis file menggunakan Python serta mengolah data yang tersimpan di dalam file. Saya juga memahami penggunaan `try-except` untuk menangani error, seperti `FileNotFoundError` dan `ValueError`. Penanganan error membantu program melewati data yang tidak valid sehingga data lainnya tetap dapat diproses dan hasil rekap dapat dihasilkan dengan benar.
