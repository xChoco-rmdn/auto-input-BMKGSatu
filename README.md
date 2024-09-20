---

# Auto Input BMKGSatu V2 >>>> https://bmkgsatu.bmkg.go.id/

Auto Input BMKGSatu adalah program otomatisasi pengisian form ME.48 yang digunakan pada stasiun meteorologi BMKG. Program ini membantu melakukan pengisian data secara otomatis ke website BMKGSatu berdasarkan input dari file Excel yang sesuai dengan template yang telah disediakan.

## Fitur Utama
- **Otomatisasi Input**: Program ini mengisi parameter cuaca dari excel ME.48 upt ke BMKG secara otomatis.
- **Integrasi File Excel**: Input data dapat diperbarui langsung dari file Excel yang sesuai dengan pengamatan cuaca.
- **Fleksibilitas Pengisian**: Dapat digunakan untuk jam pengamatan berbeda.

## Dependencies
Program ini memerlukan beberapa dependencies untuk menjalankan fungsinya, berikut adalah beberapa yang digunakan:
- `Playwright` - Digunakan untuk otomatisasi interaksi dengan browser.
- `Pandas` - Digunakan untuk memproses data dari file Excel atau CSV.
- `Tkinter` - Untuk membangun antarmuka GUI.
- `screeninfo` - Mendapatkan informasi layar yang digunakan untuk menyesuaikan tampilan browser.
- `openpyxl` - untuk membaca input file excel

Berikut untuk instalasi dependencies menggunakan `pip`:
```bash
pip install pandas playwright tkinter screeninfo openpyxl
```

## Cara Penggunaan
1. Siapkan file Excel input yang sesuai dengan format pengamatan cuaca (bisa di hubungkan dengan Form ME.48 upt) dengan nama sheet harus `input_data`.
2. Jalankan program ini, Anda dapat memilih file Excel sebagai input.
3. Program akan mengisi data dari Excel ke form BMKG Satu secara otomatis setelah klick run.

## Bagian yang Perlu Disesuaikan
Program ini memungkinkan beberapa konfigurasi untuk diubah sesuai kebutuhan pengguna. Berikut adalah bagian-bagian yang perlu diperhatikan:

1. **Nama Observer**  
   Nama observer atau pengamat yang bertugas juga dapat disesuaikan. Pada file `sandi.py`bagian dictionary `obs`, nama observer diatur sesuai dgn sdm yang ada. 
   key adalah yang ditiskan user pada excel dan value nya adalah yang sesuai dengan data pada BMKGSatu. Berikut adalah defaultnya untuk Stamet Sumbawa

```bash
obs = {
    "ramadhan": "Zulkifli Ramadhan",
    "adw": "Angga Dwi Wibowo",
    "dwi": "Dwi Harjanto",
    "risna": "Ni Putu Risna Purwandari",
    "fajar": "Fajaruddin Ash Shiddiq",
    "titis": "Titis Wicaksono",
    "hudan": "Hudan Pulung Hanasti"
}
```

## Contoh Input Excel
Program ini menerima input dalam format Excel atau CSV dengan kolom-kolom berikut (detailnya bisa cek pada `masterinput.xlsx`):
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
