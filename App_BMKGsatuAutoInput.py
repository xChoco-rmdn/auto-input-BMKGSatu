import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from autoinput import AutoInput
from sandi import obs, ww, w1w2, ci, awan_lapisan, arah_angin, cm, ch
from user_input import UserInputUpdater
from browsermanager import BrowserManager
import logging
import os



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.browser_manager = None
        self.title("Auto Input BMKG by Zulkiflirmdn")
        self.geometry("400x300")

        # Variables
        self.file_path = tk.StringVar()
        self.jam_terpilih = tk.IntVar(value=0)

        # Inisialisasi browser manager
        self.browser_manager = BrowserManager(user_data_dir='C:/Users/Administrator/Documents/autoinput')
        self.browser_manager.start_browser()

        # Create Widgets
        self.create_widgets()

    def create_widgets(self):
        """UI Components"""
        file_label = tk.Label(self, text="Pilih File (Excel/CSV):")
        file_label.pack(pady=10)

        file_entry = tk.Entry(self, textvariable=self.file_path, width=40)
        file_entry.pack(pady=5)

        browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        browse_button.pack(pady=5)

        jam_label = tk.Label(self, text="Pilih Jam Pengamatan:")
        jam_label.pack(pady=10)

        jam_selector = ttk.Combobox(self, textvariable=self.jam_terpilih, values=list(range(24)), state="readonly")
        jam_selector.pack(pady=5)
        jam_selector.current(0)

        run_button = tk.Button(self, text="Run", command=self.run_auto_input)
        run_button.pack(pady=20)

    def browse_file(self):
        """Buka dialog untuk memilih file Excel atau CSVe."""
        filename = filedialog.askopenfilename(
            title="Pilih File Excel atau CSV",
            filetypes=(("Excel Files", "*.xlsx;*.xls"), ("CSV Files", "*.csv"), ("All Files", "*.*"))
        )
        self.file_path.set(filename)
        logging.info(f"File selected: {filename}")

    def validate_file_path(self, file_path):
        """Validasi apakah path file ada dan benar."""
        if not file_path or not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found.")

    def run_auto_input(self):
        """Jalankan proses input otomatis setelah memvalidasi input file."""
        try:
            # Validasi path file menggunakan the helper method
            self.validate_file_path(self.file_path.get())

            # Default user input untuk testing (can be updated)
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

            # Perbarui user_input dari file yang dipilih
            updater = UserInputUpdater(user_input)
            sheet_name = "input_data"
            updated_user_input = updater.update_from_file(self.file_path.get(), self.jam_terpilih.get(), sheet_name)

            logging.info(f"User input after update: {updated_user_input}")

            # Mulai isi formulir dengan input_pengguna yang diperbarui
            form_filler = AutoInput(self.browser_manager.page, updated_user_input, obs, ww, w1w2, awan_lapisan, arah_angin, ci, cm, ch)
            form_filler.fill_form()

            messagebox.showinfo("Success", "Proses input form selesai!")
            logging.info("Form input process completed successfully.")

        except FileNotFoundError as e:
            messagebox.showerror("Error", str(e))
            logging.error(f"File error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    def on_exit(self):
        """Cleanup on exit."""
        self.browser_manager.close_browser()
        logging.info("Application closed.")


if __name__ == "__main__":
    app = Application()
    app.protocol("WM_DELETE_WINDOW", app.on_exit)
    app.mainloop()
