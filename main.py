from playwright.sync_api import sync_playwright
from sandi import ww, w1w2, ci, awan_lapisan, arah_angin, cm, ch

def loadpage(playwright):
    # Path to the executable Google Chrome
    # chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"  # Adjust this path for your system

    print("Launching browser with persistent context...")
    # Launch Google Chrome with the specified path
    browser = playwright.chromium.launch_persistent_context(
        user_data_dir='D:/ZUL/meta',  # Path to save session (persistent context)
        headless=False,  # Set to False to see the browser window
        # executable_path=chrome_path,  # Use Google Chrome
        args=['--window-size=1920,1080']  # Set window size
    )

    # Open the target page
    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    print("Navigating to target page...")
    page.goto("https://bmkgsatu.bmkg.go.id/meteorologi/sinoptik")

    # Wait for the page to fully load
    page.wait_for_load_state("networkidle")
    print("Page fully loaded.")

    return page

def inputx(page, user_input):
    try:
        print("Starting inputx process...")

        # 1 Jam Pengamatan
        page.locator("#input-jam div").nth(1).click()
        page.locator("#input-jam").get_by_role("textbox").fill(user_input['jam_pengamatan'])
        page.locator("#input-jam").get_by_role("textbox").press("Enter")

        # 2 Pengenal data Angin (iw)
        page.locator("#wind_indicator_iw div").nth(1).click()
        page.locator("#wind_indicator_iw").get_by_role("textbox").fill(user_input['pengenal_angin'])
        page.locator("#wind_indicator_iw").get_by_role("textbox").press("Enter")

        # 3 Arah Angin
        page.get_by_label("Arah Angin (derajat)").click()
        page.get_by_label("Arah Angin (derajat)").fill(user_input['arah_angin'])

        # 4 Kecepatan Angin
        page.get_by_label("Kecepatan Angin (knot)").click()
        page.get_by_label("Kecepatan Angin (knot)").fill(user_input['kecepatan_angin'])

        # 5 Jarak Penglihatan (Visibility)
        page.get_by_label("Jarak penglihatan mendatar (").click()
        page.get_by_label("Jarak penglihatan mendatar (").fill(user_input['jarak_penglihatan'])

        # 6 Cuaca Saat Pengamatan (ww)
        ww_value = ww.get(user_input['cuaca_pengamatan'], "00")
        page.locator("#present_weather_ww div").nth(1).click()
        page.locator("#present_weather_ww").get_by_role("textbox").fill(ww_value)
        page.locator("#present_weather_ww").get_by_role("textbox").press("Enter")

        # 7 Cuaca yang lalu (W1)
        w1_value = w1w2.get(user_input['cuaca_w1'], "0")
        page.locator("#past_weather_w1 div").nth(1).click()
        page.locator("#past_weather_w1").get_by_role("textbox").fill(w1_value)
        page.locator("#past_weather_w1").get_by_role("textbox").press("Enter")

        # 8 Cuaca yang lalu (W2)
        w2_value = w1w2.get(user_input['cuaca_w2'], "0")
        page.locator("#past_weather_w2 div").nth(1).click()
        page.locator("#past_weather_w2").get_by_role("textbox").fill(w2_value)
        page.locator("#past_weather_w2").get_by_role("textbox").press("Enter")

        # 9 Tekanan QFF
        page.get_by_label("Tekanan QFF").click()
        page.get_by_label("Tekanan QFF").fill(user_input['tekanan_qff'])

        # 10 Tekanan QFE
        page.get_by_label("Tekanan QFE").click()
        page.get_by_label("Tekanan QFE").fill(user_input['tekanan_qfe'])

        # 11 Suhu Bola Kering
        page.get_by_label("Suhu Bola Kering (℃)").click()
        page.get_by_label("Suhu Bola Kering (℃)").fill(user_input['suhu_bola_kering'])

        # 12 Suhu Bola Basah
        page.get_by_label("Suhu Bola Basah (℃)").click()
        page.get_by_label("Suhu Bola Basah (℃)").fill(user_input['suhu_bola_basah'])

        # 13 Suhu Maksimum
        page.get_by_label("Suhu Maksimum (℃)").click()
        page.get_by_label("Suhu Maksimum (℃)").fill(user_input['suhu_maksimum'])

        # 14 Suhu Minimum
        page.get_by_label("Suhu Minimum (℃)").click()
        page.get_by_label("Suhu Minimum (℃)").fill(user_input['suhu_minimum'])

        # 15 Bagian Langit Tertutup Awan (oktas)
        page.locator("#cloud_cover_oktas_m div").nth(1).click()
        page.locator("#cloud_cover_oktas_m").get_by_role("textbox").fill(user_input['oktas'])
        page.locator("#cloud_cover_oktas_m").get_by_role("textbox").press("Enter")

        # 16 Hujan Ditakar
        page.get_by_label("Hujan ditakar (mm)").click()
        page.get_by_label("Hujan ditakar (mm)").fill(user_input['hujan_ditakar'])

        # 17 CL Dominan
        cl_value = ci.get(user_input['cl_dominan'], "1")
        page.locator("#cloud_low_type_cl div").nth(1).click()
        page.locator("#cloud_low_type_cl").get_by_role("textbox").fill(cl_value)
        page.locator("#cloud_low_type_cl").get_by_role("textbox").press("Enter")

        # 18 NCL Total (Jumlah Awan Rendah)
        page.locator("#cloud_low_cover_oktas div").nth(1).click()
        page.locator("#cloud_low_cover_oktas").get_by_role("textbox").fill(user_input['ncl_total'])
        page.locator("#cloud_low_cover_oktas").get_by_role("textbox").press("Enter")

        # 19 Jenis CL Lapisan 1
        jenis_cl_lap1_value = awan_lapisan.get(user_input['jenis_cl_lapisan1'], "0")
        page.locator("div:nth-child(3) > .ant-select > .ant-select-selection").first.click()
        page.locator("div:nth-child(3) > .ant-select-search__field").first.fill(jenis_cl_lap1_value)
        page.locator("div:nth-child(3) > .ant-select-search__field").first.press("Enter")

        # 20 Jumlah CL Lapisan 1
        page.locator("div:nth-child(4) > .ant-select > .ant-select-selection").first.click()
        page.locator("div:nth-child(4) > .ant-select-search__field").first.fill(user_input['jumlah_cl_lapisan1'])
        page.locator("div:nth-child(4) > .ant-select-search__field").first.press("Enter")

        # 21 Tinggi Dasar Awan Lapisan 1
        page.locator("#cloud_low_base_1").click()
        page.locator("#cloud_low_base_1").fill(user_input['tinggi_dasar_aw_lapisan1'])

        # 22 Tinggi Puncak Awan Lapisan 1
        page.locator("#cloud_low_peak_1").click()
        page.locator("#cloud_low_peak_1").fill(user_input['tinggi_puncak_aw_lapisan1'])

        # 23 Arah Gerak Awan Lapisan 1
        arah_gerak_aw_lap1_value = arah_angin.get(user_input['arah_gerak_aw_lapisan1'], "0")
        page.locator("div:nth-child(7) > .ant-select > .ant-select-selection").first.click()
        page.locator("div:nth-child(7) > .ant-select-search__field").first.fill(arah_gerak_aw_lap1_value)
        page.locator("div:nth-child(7) > .ant-select-search__field").first.press("Enter")

        # 24 Sudut Elevasi Awan Lapisan 1
        page.locator("#cloud_elevation_1_angle_ec div").nth(1).click()
        page.locator("#cloud_elevation_1_angle_ec").get_by_role("textbox").fill(str(user_input['sudut_elevasi_aw_lapisan1']))
        page.locator("#cloud_elevation_1_angle_ec").get_by_role("textbox").press("Enter")

        # 25 Activate switch for the second cloud layer
        page.locator(".switch-icon-left > .feather").first.click()

        # 26 Jenis CL Lapisan 2
        jenis_cl_lap2_value = awan_lapisan.get(user_input['jenis_cl_lapisan2'], "0")
        page.locator("div:nth-child(3) > div:nth-child(3) > .ant-select > .ant-select-selection").first.click()
        page.locator("div:nth-child(3) > div:nth-child(3) > .ant-select-search__field").first.fill(jenis_cl_lap2_value)
        page.locator("div:nth-child(3) > div:nth-child(3) > .ant-select-search__field").first.press("Enter")

        # 27 Jumlah CL Lapisan 2
        page.locator("div:nth-child(3) > div:nth-child(4) > .ant-select > .ant-select-selection").first.click()
        page.locator("div:nth-child(3) > div:nth-child(4) > .ant-select-search__field").first.fill(user_input['jumlah_cl_lapisan2'])
        page.locator("div:nth-child(3) > div:nth-child(4) > .ant-select-search__field").first.press("Enter")

        # 28 Tinggi Puncak Awan Lapisan 2
        page.locator("#cloud_low_base_2").click()
        page.locator("#cloud_low_base_2").fill(user_input['tinggi_puncak_aw_lapisan2'])

        # 29 Arah Gerak Awan Lapisan 2
        arah_gerak_aw_lap2_value = arah_angin.get(user_input['arah_gerak_aw_lapisan2'], "0")
        page.locator("div:nth-child(3) > div:nth-child(7) > .ant-select > .ant-select-selection").click()
        page.locator("div:nth-child(3) > div:nth-child(7) > .ant-select-search__field").fill(arah_gerak_aw_lap2_value)
        page.locator("div:nth-child(3) > div:nth-child(7) > .ant-select-search__field").press("Enter")

        # 30 CM Awan Menengah
        cm_value = cm.get(user_input['cm_awan_menengah'], "1")
        page.locator("#cloud_med_type_cm div").nth(1).click()
        page.locator("#cloud_med_type_cm").get_by_role("textbox").fill(cm_value)
        page.locator("#cloud_med_type_cm").get_by_role("textbox").press("Enter")

        # 31 NCM Jumlah Awan menengah
        page.locator("#cloud_med_cover_oktas div").nth(1).click()
        page.locator("#cloud_med_cover_oktas").get_by_role("textbox").fill("1")
        page.locator("#cloud_med_cover_oktas").get_by_role("textbox").press("Enter")

        # 32 Jenis Awan Menengah
        jenis_awan_menengah_value = awan_lapisan.get(user_input['jenis_awan_menengah'], "1")
        page.locator(".col-4 > div:nth-child(3) > .ant-select > .ant-select-selection").first.click()
        page.locator(".col-4 > div:nth-child(3) > .ant-select-search__field").first.fill(jenis_awan_menengah_value)
        page.locator(".col-4 > div:nth-child(3) > .ant-select-search__field").first.press("Enter")

        # 33 Jumlah awan menengah
        page.locator(
            ".col-4 > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
        page.locator(
            ".col-4 > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill(
            "1")
        page.locator(
            ".col-4 > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press(
            "Enter")

        # 34  Tinggi Dasar Awan Menengah
        page.locator("#cloud_med_base_1").click()
        page.locator("#cloud_med_base_1").fill(user_input['tinggi_dasar_aw_cm'])

        # 35 Arah Gerak Awan CM
        arah_gerak_cm_value = arah_angin.get(user_input['arah_gerak_cm'], "0")
        page.locator("div:nth-child(6) > .ant-select > .ant-select-selection").first.click()
        page.locator("div:nth-child(6) > .ant-select-search__field").first.fill(arah_gerak_cm_value)
        page.locator("div:nth-child(6) > .ant-select-search__field").first.press("Enter")

        # 36 CH Awan Tinggi
        ch_value = ch.get(user_input['ch_awan_tinggi'], "1")
        page.locator("#cloud_high_type_ch div").nth(1).click()
        page.locator("#cloud_high_type_ch").get_by_role("textbox").fill(ch_value)
        page.locator("#cloud_high_type_ch").get_by_role("textbox").press("Enter")

        # 37 NCH jumah awan tinggi
        page.locator("#cloud_high_cover_oktas div").nth(1).click()
        page.locator("#cloud_high_cover_oktas").get_by_role("textbox").fill("1")
        page.locator("#cloud_high_cover_oktas").get_by_role("textbox").press("Enter")

        # 38 jenis awan tinggi
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").fill(
            "0")
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").press(
            "Enter")

        # 39 Jumalah awan tinggi
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").fill(
            "1")
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").press(
            "Enter")

        # 40 Tinggi Dasar Awan Tinggi
        page.locator("#cloud_high_base_1").click()
        page.locator("#cloud_high_base_1").fill(user_input['tinggi_dasar_aw_ch'])

        # 41 Arah Gerak Awan CH
        arah_gerak_ch_value = arah_angin.get(user_input['arah_gerak_ch'], "0")
        page.locator("div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(6)").click()
        page.locator("div:nth-child(3) > .ant-select-search__field").first.fill(arah_gerak_ch_value)
        page.locator("div:nth-child(3) > .ant-select-search__field").first.press("Enter")

        # 42 Penguapan
        page.get_by_label("Penguapan (mm)").click()
        page.get_by_label("Penguapan (mm)").fill(user_input['penguapan'])

        # 43 Pengenal Data Penguapan (IE)
        page.locator("#evaporation_eq_indicator_ie").get_by_role("textbox").fill(user_input['pengenal_penguapan'])
        page.locator("#evaporation_eq_indicator_ie").get_by_role("textbox").press("Enter")

        # 44 Lama Penyinaran Matahari
        page.get_by_label("Lama Penyinaran Matahari (jam)").click()
        page.get_by_label("Lama Penyinaran Matahari (jam)").fill(user_input['lama_penyinaran'])

        # 45 Keadaan Tanah
        page.locator("#land_cond div").nth(1).click()
        page.locator("#land_cond").get_by_role("textbox").fill(user_input['keadaan_tanah'])
        page.locator("#land_cond").get_by_role("textbox").press("Enter")

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
                    'jam_pengamatan': '11',
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
                    'jumlah_cl_lapisan1': '5',
                    'tinggi_dasar_aw_lapisan1': '540',
                    'tinggi_puncak_aw_lapisan1': '9000',
                    'jenis_cl_lapisan1': 'CI',
                    'arah_gerak_aw_lapisan1': 'NORTH EAST',
                    'sudut_elevasi_aw_lapisan1': 0,
                    'jenis_cl_lapisan2': 'CB',
                    'jumlah_cl_lapisan2': '4',
                    'tinggi_puncak_aw_lapisan2': '600',
                    'arah_gerak_aw_lapisan2': 'SOUTH EAST',
                    'cm_awan_menengah': 'AC',
                    'jenis_awan_menengah': 'AS',
                    'tinggi_dasar_aw_cm': '3000',
                    'arah_gerak_cm': 'EAST',
                    'ch_awan_tinggi': 'CI',
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
