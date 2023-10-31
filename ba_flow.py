from playwright.sync_api import Playwright, sync_playwright, expect
from pom.homepage_overlay import HomepageOverlay


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=10)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.expatrio.com/")
    page.get_by_role("button", name="Accept all").click()
    homepage_overlay = HomepageOverlay(page=page)
    with page.expect_popup() as page1_info:
        homepage_overlay.apply_for_value_package_overlay_locator().click()
    page1 = page1_info.value
    page1.close()
    page.get_by_role("link", name="OPEN FREE BLOCKED ACCOUNT").click()
    page.get_by_placeholder("- please choose -").click()
    page.get_by_role("option", name="University student (Master)").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_text("At least 18, younger than 23 years old").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_placeholder("Blocked Amount p/m").click()
    page.get_by_placeholder("Blocked Amount p/m").fill("100")
    page.get_by_role("button", name="Next").click()
    page.get_by_label("I want to set-up a free User Account and confirm that I have downloaded, read and agreed to Expatrio’s General Terms and Conditions and Privacy Policy.").check()
    page.get_by_label("I agree that Expatrio may send me emails with offers, updates, and promotional content. The service is free of charge and can be revoked at any time!").check()
    page.get_by_role("button", name="AGREE AND APPLY").click()
    page.get_by_placeholder("Mr.").click()
    page.get_by_role("option", name="Mr.").click()
    page.get_by_placeholder("John", exact=True).click()
    page.get_by_placeholder("John", exact=True).fill("Bobon")
    page.get_by_placeholder("John", exact=True).press("Tab")
    page.get_by_placeholder("Doe", exact=True).fill("Doe")
    page.get_by_placeholder("Doe", exact=True).press("Tab")
    page.get_by_placeholder("+49").fill("+49")
    page.get_by_placeholder("+49").press("ArrowDown")
    page.get_by_placeholder("+49").press("Enter")
    page.get_by_placeholder("+49").press("Tab")
    page.get_by_placeholder("123456789").fill("12312312312")
    page.get_by_placeholder("123456789").press("Tab")
    page.get_by_placeholder("DD/MM/YYYY").click()
    page.get_by_role("button", name="1992").click()
    page.get_by_role("button", name="Apr").click()
    page.get_by_role("button", name="1", exact=True).first.click()
    page.get_by_role("button", name="Next").click()

    # ---------------------
    context.close()
    browser.close()


def run_ba_flow():
    with sync_playwright() as playwright:
        run(playwright)


if __name__ == '__main__':
    run_ba_flow()
