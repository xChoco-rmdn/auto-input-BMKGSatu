import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from playwright.sync_api import sync_playwright
from autoinput import AutoInput
from sandi import ww, w1w2, ci, awan_lapisan, arah_angin, cm, ch, obs
from browserloader import BrowserLoader
from user_input import UserInputUpdater
import os


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Auto Input BMKG by Zulkiflirmdn")
        self.geometry("400x300")

        # Variables
        self.file_path = tk.StringVar()
        self.jam_terpilih = tk.IntVar(value=0)

        # Playwright instance untuk browser
        self.browser = None
        self.page = None

        # Jalankan Chromium saat aplikasi dimulai
        self.start_browser()

        # Create Widgets
        self.create_widgets()

    def create_widgets(self):
        # Label untuk Pemilihan File
        file_label = tk.Label(self, text="Pilih File (Excel/CSV):")
        file_label.pack(pady=10)

        # Entry untuk Jalur File
        file_entry = tk.Entry(self, textvariable=self.file_path, width=40)
        file_entry.pack(pady=5)

        # Tombol untuk Browse File
        browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        browse_button.pack(pady=5)

        # Label untuk Jam Terpilih
        jam_label = tk.Label(self, text="Pilih Jam Pengamatan:")
        jam_label.pack(pady=10)

        # Dropdown untuk Pilihan Jam (0-23)
        jam_selector = ttk.Combobox(self, textvariable=self.jam_terpilih, values=list(range(24)), state="readonly")
        jam_selector.pack(pady=5)
        jam_selector.current(0)

        # Tombol untuk Menjalankan Proses
        run_button = tk.Button(self, text="Run", command=self.run_auto_input)
        run_button.pack(pady=20)

    def browse_file(self):
        # Buka dialog untuk memilih file Excel atau CSV
        filename = filedialog.askopenfilename(
            title="Pilih File Excel atau CSV",
            filetypes=(("Excel Files", "*.xlsx;*.xls"), ("CSV Files", "*.csv"), ("All Files", "*.*"))
        )
        self.file_path.set(filename)

    def start_browser(self):
        # Menjalankan Playwright untuk membuka Chromium saat aplikasi dijalankan
        try:
            # Inisialisasi Playwright
            self.playwright = sync_playwright().start()

            # Cek dan buat folder jika belum ada
            user_data_dir = 'C:/Users/Administrator/Documents/autoinput'
            if not os.path.exists(user_data_dir):
                os.makedirs(user_data_dir)

            # Inisialisasi BrowserLoader
            self.loader = BrowserLoader(
                playwright=self.playwright,
                user_data_dir=user_data_dir, # Direktori penyimpanan data login
                headless=False
            )

            # Memuat halaman BMKGSatu
            self.page = self.loader.load_page("https://bmkgsatu.bmkg.go.id/meteorologi/sinoptik")

            # Simpan referensi browser agar tidak tertutup
            self.browser = self.loader.browser

            # Tampilkan pesan bahwa browser siap
            print("Browser sudah siap dan terbuka.")
        except Exception as e:
            messagebox.showerror("Error", f"Terdapat Error saat membuka browser: {e}")

    def run_auto_input(self):
        try:
            if not self.file_path.get():
                messagebox.showerror("Error", "File belum dipilih!")
                return

            # Cek apakah browser sudah siap
            if not self.page:
                messagebox.showerror("Error", "Browser belum siap, silakan tunggu.")
                return

            # Mengambil data user_input default
            user_input = {
                'obs_onduty': 'Ramadhan',
                'jam_pengamatan': '23',
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
                'sudut_elevasi_aw_lapisan1': '0',
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

            # Memperbarui user_input berdasarkan data pada jam yang dipilih
            updated_user_input = updater.update_from_file(self.file_path.get(), self.jam_terpilih.get())

            # Menampilkan hasil update
            print("User input setelah di-update:", updated_user_input)

            # Inisialisasi objek dengan data yang diperlukan
            form_filler = AutoInput(self.page, user_input, obs, ww, w1w2, awan_lapisan, arah_angin, ci, cm, ch)

            # Menjalankan proses pengisian form
            form_filler.fill_form()

            messagebox.showinfo("Success", "Proses input form selesai!")

        except Exception as e:
            messagebox.showerror("Error", f"Terdapat Error: {e}")


if __name__ == "__main__":
    app = Application()
    app.mainloop()
