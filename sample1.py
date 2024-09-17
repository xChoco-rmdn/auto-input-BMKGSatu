import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

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
    page.locator("div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
    page.locator("div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill("9")
    page.locator("div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press("Enter")
    # Jumlah CL Lapisan 1
    page.locator("div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
    page.locator("div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill("1")
    page.locator("div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press("Enter")
    # Tinggi dasar awan lapisan 1
    page.locator("#cloud_low_base_1").click()
    page.locator("#cloud_low_base_1").fill("540")
    # Tinggi Puncak awan lapisan 1
    page.locator("#cloud_low_peak_1").click()
    page.locator("#cloud_low_peak_1").fill("9000")
    # Arah gerak awan Lapisan 1
    page.locator("div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
    page.locator("div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill("0")
    page.locator("div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press("Enter")
    # Sudut Elevasi awan lpisan 1
    page.locator("#cloud_elevation_1_angle_ec div").nth(1).click()
    page.locator("#cloud_elevation_1_angle_ec").get_by_role("textbox").fill("1")
    page.locator("#cloud_elevation_1_angle_ec").get_by_role("textbox").press("Enter")

    # Jika awan rendah lebih dari 1 Lapisan
    page.locator(".switch-icon-left > .feather").first.click()     # aktifkan switch untuk dapat memasukan input awan lapisan 2
    # jenis CL lapisan 2
    page.locator("div:nth-child(3) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
    page.locator("div:nth-child(3) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill("8")
    page.locator("div:nth-child(3) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press("Enter")
    # Jumlah CL lapisan 2
    page.locator("div:nth-child(3) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
    page.locator("div:nth-child(3) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill("4")
    page.locator("div:nth-child(3) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press("Enter")
    # Tinggi Puncak awan lapisan 2
    page.locator("#cloud_low_base_2").click()
    page.locator("#cloud_low_base_2").fill("600")
    # Arah gerak awan Lapisan 2
    page.locator("div:nth-child(3) > div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
    page.locator("div:nth-child(3) > div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").fill("0")
    page.locator("div:nth-child(3) > div:nth-child(7) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").press("Enter")

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
    page.locator(".col-4 > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
    page.locator(".col-4 > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill("4")
    page.locator(".col-4 > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press("Enter")
    # Jumlah awan menengah
    page.locator(".col-4 > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
    page.locator(".col-4 > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill("1")
    page.locator(".col-4 > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press("Enter")
    # Tinggi dasar CM
    page.locator("#cloud_med_base_1").click()
    page.locator("#cloud_med_base_1").fill("3000")
    # arah gerak awan CM
    page.locator("div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").first.click()
    page.locator("div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.fill("0")
    page.locator("div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").first.press("Enter")

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
    page.locator("div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
    page.locator("div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").fill("0")
    page.locator("div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(3) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").press("Enter")
    # Jumalah awan tinggi
    page.locator("div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
    page.locator("div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").fill("1")
    page.locator("div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(4) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").press("Enter")
    # tinggi dasar awan tinggi
    page.locator("#cloud_high_base_1").click()
    page.locator("#cloud_high_base_1").fill("9000")
    # arah gerak awan tinggi
    page.locator("div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered").click()
    page.locator("div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").fill("0")
    page.locator("div:nth-child(3) > .card > .card-body > #collapse-row-2 > div > div:nth-child(2) > div:nth-child(6) > .ant-select > .ant-select-selection > .ant-select-selection__rendered > .ant-select-search > .ant-select-search__field__wrap > .ant-select-search__field").press("Enter")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
