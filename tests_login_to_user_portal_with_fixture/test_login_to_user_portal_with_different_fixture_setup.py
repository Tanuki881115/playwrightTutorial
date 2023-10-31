from playwright.sync_api import Playwright, sync_playwright, expect
from pom.homepage_main import Homepage
from pom.homepage_overlay import HomepageOverlay
from pom.user_portal_login_page import UserPortalLoginPage
import pytest


# setting up 'setup' on the test case
@pytest.mark.use_fixture
def test_login_diff(login_setup) -> None:

    # set setup on a variable
    page = login_setup

    # We cannot set page2 and to be re-used from the fixture like this
    with page.expect_popup() as page2_info:
        page2 = page2_info.value

    # Assertion
    page.wait_for_load_state("networkidle")
    # Adding wait for a selector to be visible
    page2.wait_for_selector("xpath=//h1[@class='title underline tour-step1']", state="attached", strict=True)

    not_visible = True
    while not_visible:
        if page2.is_visible("xpath=//h1[@class='title underline tour-step1']"):
            not_visible = False

    expect(page2.locator("#non-printable div").nth(1)).to_be_visible()
    expect(page2.get_by_role("heading", name="Hello Bobon Äöüß!")).to_be_visible()

    # Assertion using xpath and to get the text of an element
    products = page2.locator("xpath=//span[text()='Your Products']").text_content()
    assert products == "Your Products"
    print(products)

    # # Expect does not accept the default time out
    # # It has its own time out but we can set it separately
    # expect(page2.get_by_role("heading", name="Hello Bobon Äöüß!")).to_be_hidden(timeout=8000)

    expect(page2.get_by_text("© 2023 | Banking services are provided by our partner Aion Bank")).to_be_visible()

    print('Success!')

    # ---------------------
    # context.close()
    # browser.close()


if __name__ == '__main__':
    with sync_playwright() as playwright:
        test_login_diff(playwright)

