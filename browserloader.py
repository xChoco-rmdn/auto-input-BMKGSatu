from playwright.sync_api import Playwright
from screeninfo import get_monitors  # Untuk mendapatkan ukuran layar


class BrowserLoader:
    def __init__(self, playwright: Playwright, user_data_dir: str, headless: bool = False):
        """
        Inisialisasi BrowserLoader dengan Playwright dan pengaturan browser.

        Args:
            playwright (Playwright): Objek Playwright yang digunakan untuk meluncurkan browser.
            user_data_dir (str): Path ke direktori data pengguna untuk konteks persisten.
            headless (bool): Menentukan apakah browser berjalan dalam mode headless (default: False).
        """
        self.playwright = playwright
        self.user_data_dir = user_data_dir
        self.headless = headless
        self.screen_width, self.screen_height = get_monitors()[0].width, get_monitors()[0].height
        self.browser = None # untuk menyimpan objek browser

    def load_page(self, url: str):
        """
        Meluncurkan browser dengan konteks persisten dan memuat halaman target.

        Args:
            url (str): URL dari halaman yang ingin diload.

        Returns:
            page (playwright.sync_api.Page): Objek halaman Playwright yang diload.
        """
        print("Launching browser with persistent context...")

        # Meluncurkan browser dengan konteks persisten (session tersimpan)
        browser = self.playwright.chromium.launch_persistent_context(
            user_data_dir=self.user_data_dir,  # Path ke direktori data pengguna
            headless=self.headless,  # Apakah berjalan dalam mode headless
            args=['--start-fullscreen']  # Menjalankan dalam mode fullscreen
        )

        # Ambil halaman pertama yang terbuka atau buka halaman baru jika tidak ada
        page = browser.pages[0] if browser.pages else browser.new_page()

        # Atur ukuran tampilan browser ke layar penuh
        page.set_viewport_size({"width": self.screen_width, "height": self.screen_height})
        print(f"Navigating to {url}...")
        page.goto(url)

        # Tunggu hingga halaman sepenuhnya terload
        page.wait_for_load_state("networkidle")
        print("Page fully loaded.")

        return page
