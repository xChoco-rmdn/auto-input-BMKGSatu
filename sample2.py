from playwright.sync_api import sync_playwright


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

def inputx(page):
    try:
        print("Starting inputx process...")

        # pilih jam pengamatan
        page.locator("#input-jam div").nth(1).click()
        page.locator("#input-jam").get_by_role("textbox").fill("09")
        page.locator("#input-jam").get_by_role("textbox").press("ArrowDown")
        page.locator("#input-jam").get_by_role("textbox").press("Enter")
        # Pengenal data Angin (iw)
        page.locator("#wind_indicator_iw div").nth(1).click()
        page.locator("#wind_indicator_iw").get_by_role("textbox").fill("3")
        page.locator("#wind_indicator_iw").get_by_role("textbox").press("ArrowDown")
        page.locator("#wind_indicator_iw").get_by_role("textbox").press("Enter")
        # Arah angin
        page.get_by_label("Arah Angin (derajat)").click()
        page.get_by_label("Arah Angin (derajat)").fill("150")
        # Kecepatan Angin
        page.get_by_label("Kecepatan Angin (knot)").click()
        page.get_by_label("Kecepatan Angin (knot)").fill("11")
        # Visibilty
        page.get_by_label("Jarak penglihatan mendatar (").click()
        page.get_by_label("Jarak penglihatan mendatar (").fill("10")
        # Cuaca Saat Pengamatan (ww)
        page.locator("#present_weather_ww div").nth(1).click()
        page.locator("#present_weather_ww").get_by_role("textbox").fill("60")
        page.locator("#present_weather_ww").get_by_role("textbox").press("ArrowDown")
        page.locator("#present_weather_ww").get_by_role("textbox").press("Enter")
        # Cuaca yang lalu (W1)
        page.locator("#past_weather_w1 div").nth(1).click()
        page.locator("#past_weather_w1").get_by_role("textbox").fill("6")
        page.locator("#past_weather_w1").get_by_role("textbox").press("ArrowDown")
        page.locator("#past_weather_w1").get_by_role("textbox").press("Enter")
        # Cuaca yang lalu (W2)
        page.locator("#past_weather_w2 div").nth(1).click()
        page.locator("#past_weather_w2").get_by_role("textbox").fill("2")
        page.locator("#past_weather_w2").get_by_role("textbox").press("ArrowDown")
        page.locator("#past_weather_w2").get_by_role("textbox").press("Enter")
        # QFF
        page.get_by_label("Tekanan QFF").click()
        page.get_by_label("Tekanan QFF").fill("1002.3")
        # QFE
        page.get_by_label("Tekanan QFE").click()
        page.get_by_label("Tekanan QFE").fill("1001.8")
        # Suhu Bola kering
        page.get_by_label("Suhu Bola Kering (℃)").click()
        page.get_by_label("Suhu Bola Kering (℃)").fill("25.3")
        # Suhu Bola Basah
        page.get_by_label("Suhu Bola Basah (℃)").click()
        page.get_by_label("Suhu Bola Basah (℃)").fill("22.3")
        # Suhu Maksimum
        page.get_by_label("Suhu Maksimum (℃)").click()
        page.get_by_label("Suhu Maksimum (℃)").fill("2323.4")
        # Suhu Minimum
        page.get_by_label("Suhu Minimum (℃)").click()
        page.get_by_label("Suhu Minimum (℃)").fill("2323.4")
        # Bagian Langit Tertutup Awan (oktas)
        page.locator("#cloud_cover_oktas_m div").nth(1).click()
        page.locator("#cloud_cover_oktas_m").get_by_role("textbox").fill("6")
        page.locator("#cloud_cover_oktas_m").get_by_role("textbox").press("ArrowDown")
        page.locator("#cloud_cover_oktas_m").get_by_role("textbox").press("Enter")
        # Hujan Ditakar
        page.get_by_label("Hujan ditakar (mm)").click()
        page.get_by_label("Hujan ditakar (mm)").fill("20")

        # Bagian Awan Rendah
        # CL Dominan
        page.locator("#cloud_low_type_cl div").nth(1).click()
        page.locator("#cloud_low_type_cl").get_by_role("textbox").fill("9")
        page.locator("#cloud_low_type_cl").get_by_role("textbox").press("Enter")

        # NCL total
        page.locator("#cloud_low_cover_oktas div").nth(1).click()
        page.locator("#cloud_low_cover_oktas").get_by_role("textbox").fill("5")
        page.locator("#cloud_low_cover_oktas").get_by_role("textbox").press("Enter")

        # Jenis CL Lapisan 1
        page.locator(
            "div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
        page.locator(
            "div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill(
            "9")
        page.locator(
            "div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press(
            "Enter")
        # Jumlah CL Lapisan 1
        page.locator(
            "div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
        page.locator(
            "div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill(
            "1")
        page.locator(
            "div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press(
            "Enter")
        # Tinggi dasar awan lapisan 1
        page.locator("#cloud_low_base_1").click()
        page.locator("#cloud_low_base_1").fill("540")
        # Tinggi Puncak awan lapisan 1
        page.locator("#cloud_low_peak_1").click()
        page.locator("#cloud_low_peak_1").fill("9000")
        # Arah gerak awan Lapisan 1
        page.locator(
            "div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
        page.locator(
            "div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill(
            "0")
        page.locator(
            "div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press(
            "Enter")
        # Sudut Elevasi awan lpisan 1
        page.locator("#cloud_elevation_1_angle_ec div").nth(1).click()
        page.locator("#cloud_elevation_1_angle_ec").get_by_role("textbox").fill("1")
        page.locator("#cloud_elevation_1_angle_ec").get_by_role("textbox").press("Enter")

        # Jika awan rendah lebih dari 1 Lapisan
        page.locator(
            ".switch-icon-left > .feather").first.click()  # aktifkan switch untuk dapat memasukan input awan lapisan 2
        # jenis CL lapisan 2
        page.locator(
            "div:nth-child(3) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
        page.locator(
            "div:nth-child(3) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill(
            "8")
        page.locator(
            "div:nth-child(3) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press(
            "Enter")
        # Jumlah CL lapisan 2
        page.locator(
            "div:nth-child(3) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
        page.locator(
            "div:nth-child(3) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill(
            "4")
        page.locator(
            "div:nth-child(3) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press(
            "Enter")
        # Tinggi Puncak awan lapisan 2
        page.locator("#cloud_low_base_2").click()
        page.locator("#cloud_low_base_2").fill("600")
        # Arah gerak awan Lapisan 2
        page.locator(
            "div:nth-child(3) > div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
        page.locator(
            "div:nth-child(3) > div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").fill(
            "0")
        page.locator(
            "div:nth-child(3) > div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").press(
            "Enter")

        # Bagian Awan Menengah
        # CM awan menengah
        page.locator("#cloud_med_type_cm div").nth(1).click()
        page.locator("#cloud_med_type_cm").get_by_role("textbox").fill("1")
        page.locator("#cloud_med_type_cm").get_by_role("textbox").press("Enter")
        # NCM Jumlah Awan menengah
        page.locator("#cloud_med_cover_oktas div").nth(1).click()
        page.locator("#cloud_med_cover_oktas").get_by_role("textbox").fill("1")
        page.locator("#cloud_med_cover_oktas").get_by_role("textbox").press("Enter")
        # jenis awan menengah
        page.locator(
            ".col-4 > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
        page.locator(
            ".col-4 > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill(
            "4")
        page.locator(
            ".col-4 > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press(
            "Enter")
        # Jumlah awan menengah
        page.locator(
            ".col-4 > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
        page.locator(
            ".col-4 > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill(
            "1")
        page.locator(
            ".col-4 > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press(
            "Enter")
        # Tinggi dasar CM
        page.locator("#cloud_med_base_1").click()
        page.locator("#cloud_med_base_1").fill("3000")
        # arah gerak awan CM
        page.locator(
            "div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
        page.locator(
            "div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill(
            "0")
        page.locator(
            "div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press(
            "Enter")

        # Bagian awan tinggi
        # Ch awan tinggi
        page.locator("#cloud_high_type_ch div").nth(1).click()
        page.locator("#cloud_high_type_ch").get_by_role("textbox").fill("1")
        page.locator("#cloud_high_type_ch").get_by_role("textbox").press("Enter")
        # NCH jumah awan menengah
        page.locator("#cloud_high_cover_oktas div").nth(1).click()
        page.locator("#cloud_high_cover_oktas").get_by_role("textbox").fill("1")
        page.locator("#cloud_high_cover_oktas").get_by_role("textbox").press("Enter")
        # jenis awan tinggi
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").fill(
            "0")
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").press(
            "Enter")
        # Jumalah awan tinggi
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").fill(
            "1")
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").press(
            "Enter")
        # tinggi dasar awan tinggi
        page.locator("#cloud_high_base_1").click()
        page.locator("#cloud_high_base_1").fill("9000")
        # arah gerak awan tinggi
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").fill(
            "0")
        page.locator(
            "div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").press(
            "Enter")

        # Penguapan
        page.get_by_label("Penguapan (mm)").click()
        page.get_by_label("Penguapan (mm)").fill("7.72")
        # Pengenal Data Penguapan(IE)
        page.locator("#evaporation_eq_indicator_ie").get_by_role("textbox").fill("0")
        page.locator("#evaporation_eq_indicator_ie").get_by_role("textbox").press("Enter")
        # Lama Penyinaran Matahari
        page.get_by_label("Lama Penyinaran Matahari (jam)").click()
        page.get_by_label("Lama Penyinaran Matahari (jam)").fill("7.76")

        # Keadaan tanah tanah
        page.locator("#land_cond div").nth(1).click()
        page.locator("#land_cond").get_by_role("textbox").fill("0")
        page.locator("#land_cond").get_by_role("textbox").press("Enter")
        # preview
        page.get_by_role("button", name="Preview").click()

    except Exception as e:
        print(f"An error occurred in inputx: {e}")


# Start Playwright
with sync_playwright() as playwright:
    # Run the 'loadpage' function to open the browser and page
    page = loadpage(playwright)  # Corrected the function name here

    # Loop to allow user input and execute 'inputx' multiple times
    while True:
        command = input("Enter command (type 'run' to run the input function, 'exit' to close): ")
        if command == "run":
            try:
                inputx(page)  # Execute inputx function
                print("Executed inputx function.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif command == "exit":
            print("Closing browser...")
            page.context.close()  # Close the browser and context
            break
        else:
            print("Unrecognized command, please try again.")
