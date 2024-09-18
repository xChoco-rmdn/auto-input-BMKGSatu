from playwright.sync_api import sync_playwright
from autoinput import AutoInput
from sandi import ww, w1w2, ci, awan_lapisan, arah_angin, cm, ch, obs
from browserloader import BrowserLoader
from user_input import UserInputUpdater

with sync_playwright() as playwright:
    # Inisialisasi BrowserLoader
    loader = BrowserLoader(
        playwright=playwright,
        user_data_dir='/Users/mb2/learn-python/autoss/.venv/bin/python /Users/mb2/learn-python/auto-input-BMKGSatu/', # untuk menyimpan data login
        headless=False
    )

    # Load Website BMKGSatu
    page = loader.load_page("https://bmkgsatu.bmkg.go.id/meteorologi/sinoptik")

    while True:
        command = input("Masukan Perintah (Ketik 'run' Untuk Menjalankan Input, 'exit' Untuk Menutup): ")
        if command == "run":
            try:
                # need to make this auto update user input -_-
                user_input = {
                    'obs_onduty': 'Ramadhan',
                    'jam_pengamatan': '21',
                    'pengenal_angin': '3',
                    'arah_angin': '150',
                    'kecepatan_angin': '11',
                    'jarak_penglihatan': '10',
                    'cuaca_pengamatan': 'MIST',
                    'cuaca_w1': 'RAIN',
                    'cuaca_w2': 'TS',
                    'tekanan_qff': '1002.3',
                    'tekanan_qfe': '1001.8',
                    'suhu_bola_kering': '25.3',
                    'suhu_bola_basah': '22.3',
                    'suhu_maksimum': '23.4',
                    'suhu_minimum': '23.4',
                    'oktas': '6',
                    'hujan_ditakar': '20',
                    'cl_dominan': 'CU',
                    'ncl_total': '6',
                    'jenis_cl_lapisan1': 'SC',
                    'jumlah_cl_lapisan1': '5',
                    'tinggi_dasar_aw_lapisan1': '540',
                    'tinggi_puncak_aw_lapisan1': '',
                    'arah_gerak_aw_lapisan1': 'NORTH EAST',
                    'sudut_elevasi_aw_lapisan1': 0,
                    'jenis_cl_lapisan2': 'CU',
                    'jumlah_cl_lapisan2': '4',
                    'tinggi_dasar_aw_lapisan2': '600',
                    'arah_gerak_aw_lapisan2': 'SOUTH EAST',
                    'cm_awan_menengah': 'AC',
                    'ncm_awan_menengah': '1',
                    'jenis_awan_menengah': 'AS',
                    'tinggi_dasar_aw_cm': '3000',
                    'arah_gerak_cm': 'EAST',
                    'ch_awan_tinggi': 'CI',
                    'nch_awan_tinggi': '5',
                    'tinggi_dasar_aw_ch': '9000',
                    'arah_gerak_ch': 'WEST',
                    'penguapan': '7.72',
                    'pengenal_penguapan': '0',
                    'lama_penyinaran': '7.76',
                    'keadaan_tanah': '0'
                }
                # Inisialisasi class dengan dictionary user_input
                updater = UserInputUpdater(user_input)

                # Path ke file Excel
                file_path = 'D:/ZUL/priject py/masterinput.xlsx' # Pilih Lokasi file excel untuk inputan data

                # Jam yang ingin diperbarui
                jam_terpilih = 23

                # Memperbarui user_input berdasarkan data pada jam yang dipilih
                updated_user_input = updater.update_from_file(file_path, jam_terpilih)

                # Menampilkan hasil update
                print("User input setelah di-update:", updated_user_input)
                # Inisialisasi objek dengan data yang diperlukan
                form_filler = AutoInput(page, user_input, obs, ww, w1w2, awan_lapisan, arah_angin, ci, cm, ch)

                # Menjalankan proses pengisian form
                form_filler.fill_form()

            except Exception as e:
                print(f"Terdapat Error: {e}")

        elif command == "exit":
            print("Menutup browser...")
            page.context.close()
            break
        else:
            print("Perintah Salah, Silahkan Coba lagi!")
