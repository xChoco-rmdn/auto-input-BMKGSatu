---

# Auto Input BMKGSatu V2 >>>> https://bmkgsatu.bmkg.go.id/

Auto Input BMKG Satu adalah program otomatisasi pengisian formulir cuaca harian yang digunakan pada stasiun meteorologi BMKG, sesuai dengan form ME.48. Program ini membantu melakukan pengisian data cuaca, seperti suhu, kecepatan angin, penguapan, dan banyak lagi, secara otomatis ke sistem BMKG Satu berdasarkan input dari file Excel yang sesuai dengan template yang telah disediakan.

## Fitur Utama
- **Otomatisasi Input**: Program ini mengisi formulir cuaca harian BMKG secara otomatis.
- **Integrasi File Excel**: Input data dapat diperbarui langsung dari file Excel yang sesuai dengan pengamatan cuaca.
- **Fleksibilitas Pengisian**: Dapat digunakan untuk jam pengamatan berbeda sesuai dengan jadwal stasiun.

## Dependencies
Program ini memerlukan beberapa dependencies untuk menjalankan fungsinya, berikut adalah beberapa yang digunakan:
- `Playwright` - Digunakan untuk otomatisasi interaksi dengan browser.
- `Pandas` - Digunakan untuk memproses data dari file Excel atau CSV.
- `Tkinter` - Untuk membangun antarmuka GUI.
- `screeninfo` - Mendapatkan informasi layar yang digunakan untuk menyesuaikan tampilan browser.

Berikut contoh instalasi dependencies menggunakan `pip`:
```bash
pip install pandas playwright tkinter screeninfo
```

## Cara Penggunaan
1. Siapkan file Excel input yang sesuai dengan format pengamatan cuaca (Form ME.48).
2. Jalankan program ini, Anda dapat memilih file Excel yang sesuai dan mengatur jam pengamatan.
3. Program akan mengisi data dari Excel ke form BMKG Satu secara otomatis.

## Contoh Input Excel
Program ini menerima input dalam format Excel atau CSV dengan kolom-kolom berikut:
- `Jam`: Waktu pengamatan (0-23)
- `Suhu_bola_kering`, `Suhu_bola_basah`, `Suhu_maksimum`, `Suhu_minimum`: Kolom untuk pengamatan suhu
- `Tekanan_qff`, `Tekanan_qfe`: Kolom untuk tekanan udara
- `Arah_angin`, `Kecepatan_angin`: Kolom untuk angin
- `Cuaca_pengamatan`, `Cuaca_w1`, `Cuaca_w2`: Kolom untuk kondisi cuaca
- dan beberapa kolom pengamatan lainnya.

Pastikan file Anda memiliki format yang sesuai agar proses input otomatis dapat berjalan dengan lancar.

## Developer
Project ini dikembangkan oleh **Zulkiflirmdn** dari Stasiun Meteorologi Sumbawa. Jika Anda memiliki pertanyaan lebih lanjut, silakan hubungi melalui email di:  
zulkifli.ramadhan@bmkg.go.id

mantaapppp <3

---
