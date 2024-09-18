import pandas as pd


class UserInputUpdater:
    def __init__(self, user_input):
        """
        Inisialisasi class dengan dictionary user_input.
        """
        self.user_input = user_input

    def update_from_excel(self, file_path, jam_terpilih):
        """
        Memperbarui dictionary user_input berdasarkan file Excel dan jam yang dipilih.

        Args:
            file_path (str): Path ke file Excel yang berisi data pengamatan.
            jam_terpilih (int): Jam yang ingin diperbarui (0-23).

        Returns:
            dict: Dictionary yang sudah diperbarui.
        """
        # Membaca file Excel dari sheet bernama 'data_input'
        df = pd.read_excel(file_path, sheet_name='data_input')

        # Filter data berdasarkan jam pengamatan
        data_jam = df[df['Jam'] == jam_terpilih]

        # Cek jika data jam ditemukan
        if data_jam.empty:
            print(f"Data untuk jam {jam_terpilih} tidak ditemukan!")
            return self.user_input

        # Mengiterasi setiap kolom di baris tersebut untuk memperbarui dictionary
        for column in data_jam.columns:
            if column in self.user_input and column != 'Jam':  # Jangan update kolom 'Jam'
                self.user_input[column] = data_jam[column].values[0]  # Update nilai di dict

        return self.user_input

    def get_user_input(self):
        """
        Mengembalikan dictionary user_input saat ini.

        Returns:
            dict: Dictionary user_input saat ini.
        """
        return self.user_input


# Contoh penggunaan
if __name__ == "__main__":
    # Dictionary asli yang ingin diperbarui
    user_input = {
        'obs_onduty': 'Ramadhan',
        'jam_pengamatan': '20',
        'pengenal_angin': '3',
        'arah_angin': '150',
        'kecepatan_angin': '11',
        'jarak_penglihatan': '10',
        'cuaca_pengamatan': 'MIST',
        'cuaca_w1': 'RAIN',
        'cuaca_w2': 'TS'
    }

    # Inisialisasi class dengan dictionary user_input
    updater = UserInputUpdater(user_input)

    # Path ke file Excel
    file_path = 'user_input_data.xlsx'

    # Jam yang ingin diperbarui
    jam_terpilih = 10

    # Memperbarui user_input berdasarkan data pada jam yang dipilih
    updated_user_input = updater.update_from_excel(file_path, jam_terpilih)

    # Menampilkan hasil update
    print("User input setelah di-update:", updated_user_input)
