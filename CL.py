from playwright.sync_api import sync_playwright
from sandi import ww, w1w2, ci, awan_lapisan, arah_angin, cm, ch, obs
from screeninfo import get_monitors
from datetime import datetime
import pyautogui


def loadpage(playwright):
    # Path to the executable Google Chrome
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # Adjust this path for your system
    screen_width, screen_height = get_monitors()[0].width, get_monitors()[0].height

    print("Launching browser with persistent context...")

    # Launch Google Chrome with the specified path
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir='/Users/mb2/learn-python/autoss/.venv/bin/python /Users/mb2/learn-python/auto-input-BMKGSatu/',  # Path to save session (persistent context)
        headless=False,  # Set to False to see the browser window
        executable_path=chrome_path,  # Use Google Chrome
        args=['--start-fullscreen']  # Set window size
    )

    # Get the first page that opened in the persistent context
    page = browser.pages[0] if browser.pages else browser.new_page()

    # Set the viewport size (fullscreen)
    page.set_viewport_size({"width": screen_width, "height": screen_height})
    print("Navigating to target page...")
    page.goto("https://bmkgsatu.bmkg.go.id/meteorologi/sinoptik")

    # Wait for the page to fully load
    page.wait_for_load_state("networkidle")
    print("Page fully loaded.")

    return page


def input_cloud_layer_2(page, user_input, awan_lapisan, arah_angin):
    """
    Mengisi data untuk lapisan awan kedua (CL Lapisan 2) berdasarkan user_input.

    Args:
        page: Halaman Playwright yang sedang aktif.
        user_input: Dictionary berisi input data dari pengguna.
        awan_lapisan: Dictionary yang berisi jenis awan dan nilai-nilainya.
        arah_angin: Dictionary yang berisi arah angin dan nilai-nilainya.
    """
    # 25 Activate switch for the second cloud layer
    page.locator(".switch-icon-left > .feather").first.click()

    # 26 Jenis CL Lapisan 2
    jenis_cl_lap2_value = awan_lapisan.get(user_input['jenis_cl_lapisan2'], "0")
    page.locator("div:nth-child(3) > div:nth-child(3) > .ant-select > .ant-select-selection").first.click()
    page.get_by_role("option", name=jenis_cl_lap2_value).click()

    # # 27 Jumlah CL Lapisan 2
    # page.locator("div:nth-child(3) > div:nth-child(4) > .ant-select > .ant-select-selection").first.click()
    # page.locator("div:nth-child(3) > div:nth-child(4) > .ant-select-search__field").first.fill(user_input['jumlah_cl_lapisan2'])
    # page.locator("div:nth-child(3) > div:nth-child(4) > .ant-select-search__field").first.press("Enter")

    # 28 Tinggi Dasar Awan Lapisan 2
    page.locator("#cloud_low_base_2").click()
    page.locator("#cloud_low_base_2").fill(user_input['tinggi_dasar_aw_lapisan2'])

    # # 29 Arah Gerak Awan Lapisan 2
    # arah_gerak_aw_lap2_value = arah_angin.get(user_input['arah_gerak_aw_lapisan2'], "0")
    # page.locator("div:nth-child(3) > div:nth-child(7) > .ant-select > .ant-select-selection").click()
    # page.locator("div:nth-child(3) > div:nth-child(7) > .ant-select-search__field").fill(arah_gerak_aw_lap2_value)
    # page.locator("div:nth-child(3) > div:nth-child(7) > .ant-select-search__field").press("Enter")


def inputx(page, user_input):
    try:
        print("Starting inputx process...")

        # Pilih stasiun
        page.locator("#select-station div").nth(1).click()
        page.get_by_role("option", name="Stasiun Meteorologi Sultan").click() #nama stasiun bisa disesuaikan

        # pilih observer on duty
        obs_onduty_value = obs.get(user_input['obs_onduty'].lower(), "Zulkifli Ramadhan")
        page.locator("#select-observer div").nth(1).click()
        page.get_by_role("option", name=obs_onduty_value).click()

        # Tanggal Pengamatan
        today = datetime.now()
        tgl_harini = f"/{today.month}/{today.year} (Today)"
        page.locator("#input-datepicker__value_").click()
        page.get_by_label(tgl_harini).click()

        # 1 Jam Pengamatan
        page.locator("#input-jam div").nth(1).click()
        page.locator("#input-jam").get_by_role("textbox").fill(user_input['jam_pengamatan'])
        page.locator("#input-jam").get_by_role("textbox").press("Enter")

        # conditional pengisian parameter tertentu pada jam-jam penting
        jam_penting = int(user_input['jam_pengamatan'])

        if jam_penting == 0:
            # 14 Suhu Minimum
            page.get_by_label("Suhu Minimum (℃)").click()
            page.get_by_label("Suhu Minimum (℃)").fill(user_input['suhu_minimum'])

            # 16 Hujan Ditakar
            page.get_by_label("Hujan ditakar (mm)").click()
            page.get_by_label("Hujan ditakar (mm)").fill(user_input['hujan_ditakar'])

            # 42 Penguapan
            page.get_by_label("Penguapan (mm)").click()
            page.get_by_label("Penguapan (mm)").fill(user_input['penguapan'])

            # 43 Pengenal Data Penguapan (IE)
            page.locator("#evaporation_eq_indicator_ie").get_by_role("textbox").fill(user_input['pengenal_penguapan'])
            page.locator("#evaporation_eq_indicator_ie").get_by_role("textbox").press("Enter")

            # 44 Lama Penyinaran Matahari
            page.get_by_label("Lama Penyinaran Matahari (jam)").click()
            page.get_by_label("Lama Penyinaran Matahari (jam)").fill(user_input['lama_penyinaran'])

        elif jam_penting == 12:
            # 13 Suhu Maksimum
            page.get_by_label("Suhu Maksimum (℃)").click()
            page.get_by_label("Suhu Maksimum (℃)").fill(user_input['suhu_maksimum'])

            # 16 Hujan Ditakar
            page.get_by_label("Hujan ditakar (mm)").click()
            page.get_by_label("Hujan ditakar (mm)").fill(user_input['hujan_ditakar'])

        elif jam_penting in [3, 6, 9, 15, 18, 21]:
            # 16 Hujan Ditakar
            page.get_by_label("Hujan ditakar (mm)").click()
            page.get_by_label("Hujan ditakar (mm)").fill(user_input['hujan_ditakar'])

        else:
            print("Jam Pengamatan tidak termasuk jam penting.")

        # 17 CL Dominan
        cl_value = ci.get(user_input['cl_dominan'], "1")
        page.locator("#cloud_low_type_cl div").nth(1).click()
        if cl_value == "1":
            page.get_by_role("option", name="1 - cumulus humilis atau").click()
        else:
            page.locator("#cloud_low_type_cl").get_by_role("textbox").fill(cl_value)
            page.locator("#cloud_low_type_cl").get_by_role("textbox").press("Enter")

        # 18 NCL Total (Jumlah Awan Rendah)
        page.locator("#cloud_low_cover_oktas div").nth(1).click()
        page.locator("#cloud_low_cover_oktas").get_by_role("textbox").fill(user_input['ncl_total'])
        page.locator("#cloud_low_cover_oktas").get_by_role("textbox").press("Enter")

        # 19 Jenis CL Lapisan 1
        jenis_cl_lap1_value = awan_lapisan.get(user_input['jenis_cl_lapisan1'], "0")
        print(jenis_cl_lap1_value)
        page.locator("div:nth-child(3) > .ant-select > .ant-select-selection").first.click()
        page.get_by_role("option", name=jenis_cl_lap1_value).click()

        # 20 Jumlah CL Lapisan 1
        page.locator("div:nth-child(4) > .ant-select > .ant-select-selection").first.click()
        page.locator("div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill(user_input['jumlah_cl_lapisan1'])
        page.get_by_role("option", name="oktas").click()

        # 21 Tinggi Dasar Awan Lapisan 1
        page.locator("#cloud_low_base_1").click()
        page.locator("#cloud_low_base_1").fill(user_input['tinggi_dasar_aw_lapisan1'])

        # # 23 Arah Gerak Awan Lapisan 1
        # arah_gerak_aw_lap1_value = arah_angin.get(user_input['arah_gerak_aw_lapisan1'], "0")
        # page.locator("div:nth-child(7) > .ant-select > .ant-select-selection").first.click()
        # page.locator("div:nth-child(7) > .ant-select-search__field").first.fill(arah_gerak_aw_lap1_value)
        # page.locator("div:nth-child(7) > .ant-select-search__field").first.press("Enter")

        print()
        if jenis_cl_lap1_value == "- cumulus (Cu)" or "- cumulonimbus (Cb)":
            # 22 Tinggi Puncak Awan Lapisan 1
            page.locator("#cloud_low_peak_1").click()
            page.locator("#cloud_low_peak_1").fill(user_input['tinggi_puncak_aw_lapisan1'])

            # 24 Sudut Elevasi Awan Lapisan 1
            page.locator("#cloud_elevation_1_angle_ec div").nth(1).click()
            page.locator("#cloud_elevation_1_angle_ec").get_by_role("textbox").fill(
                str(user_input['sudut_elevasi_aw_lapisan1']))
            page.locator("#cloud_elevation_1_angle_ec").get_by_role("textbox").press("Enter")

            input_cloud_layer_2(page, user_input, awan_lapisan, arah_angin)

        # Preview
        page.get_by_role("button", name="Preview").click()

        print("Form input successfully executed.")

    except Exception as e:
        print(f"An error occurred in inputx: {e}")

with sync_playwright() as playwright:
    page = loadpage(playwright)

    while True:
        command = input("Enter command (type 'run' to run the input function, 'exit' to close): ")
        if command == "run":
            try:
                user_input = {
                    'obs_onduty': 'Ramadhan',
                    'jam_pengamatan': '10',
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
                    'tinggi_puncak_aw_lapisan1': '9000',
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

                inputx(page, user_input)
                print("Executed inputx function.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif command == "exit":
            print("Closing browser...")
            page.context.close()
            break
        else:
            print("Unrecognized command, please try again.")
