import pandas as pd


class UserInputUpdater:
    def __init__(self, user_input):
        """
        Inisialisasi dengan data `user_input` yang akan di-update.

        Args:
            user_input (dict): Dictionary berisi data user_input yang akan diperbarui.
        """
        self.user_input = user_input

    def update_from_file(self, file_path, jam_terpilih):
        """
        Update user_input dari file Excel atau CSV berdasarkan jam terpilih.

        Args:
            file_path (str): Path ke file (Excel atau CSV).
            jam_terpilih (int): Jam pengamatan yang ingin diperbarui.

        Returns:
            dict: Dictionary user_input yang sudah diperbarui.
        """
        # Tentukan format file (CSV atau Excel)
        if file_path.endswith('.csv'):
            data = pd.read_csv(file_path)
        else:
            data = pd.read_excel(file_path)

        # Cari baris yang sesuai dengan jam terpilih
        row = data[data['Jam'] == jam_terpilih]

        if row.empty:
            raise ValueError(f"Jam {jam_terpilih} tidak ditemukan di file.")

        # Update user_input dengan data dari row yang ditemukan
        for key in self.user_input:
            if key in row.columns:
                self.user_input[key] = row.iloc[0][key]

        return self.user_input
