from playwright.sync_api import Playwright, sync_playwright, expect
from pom.homepage_main import Homepage
from pom.homepage_overlay import HomepageOverlay
from pom.user_portal_login_page import UserPortalLoginPage
import pytest


"""
# setting up data driven param
# handling for the data driven test which is supposed to be failed
# For data set 2 and 3
We can specify more than 1 @pytest.mark.parametrize() which contain more than 1 data
e.g.: if we want to test with different combination of email and password
We can specify the 1st one only for email
@pytest.mark.parametrize("email, [
    ("tito+mob01@expatrio.com"),
    pytest.param("tito+mob02@expatrio.com", marks=pytest.mark.xfail),
    pytest.param("tito+mob03@expatrio.com", marks=pytest.mark.xfail),
])

We can specify the 2nd one only for password
@pytest.mark.parametrize("password", [
    ("Bobon@mob01"),
    pytest.param("Bobon@mob02", marks=pytest.mark.xfail),
    pytest.param("Bobon@mob03", marks=pytest.mark.xfail),
])

What is gonna happened here is for email == tito+mob01@expatrio.com,
It will try to iterate with all the password
Then it will go to the next email and iterate with all the password
In this case we will have 9 test cases run
This way we can cover more test
"""


# setting up 'setup' on the test case
@pytest.mark.use_fixture
@pytest.mark.parametrize("email, password", [
    ("tito+mob01@expatrio.com", "Bobon@mob01"),
    pytest.param("tito+mob02@expatrio.com", "Bobon@mob02", marks=pytest.mark.xfail),
    pytest.param("tito+mob03@expatrio.com", "Bobon@mob03", marks=pytest.mark.xfail),
])
def test_login(setup, email, password) -> None:

    # set setup on a variable
    page = setup

    # # Setting default time out
    # page.set_default_timeout(3000)

    # # pause() will pause the operation at any given point
    # # It is use to debugging when at some point our test is failing
    # page.pause()

    # Initializing Homepage class
    homepage = Homepage(page=page)

    # Using POM to navigate to Homepage
    # page.goto("https://www.expatrio.com/")
    homepage.navigate_to_homepage()

    # Homepage
    # Adding time out on each operation
    # Adding time out (in milliseconds) can be added when performing click or inputting value in a field
    # page.get_by_role("button", name="Accept all").click(timeout=3000)
    # Using POM to Accept All Coockies
    homepage.accept_all_cookies_locator().click(timeout=3000)

    # wait_for_load_state("networkidle") means we will wait until there is no network activity
    page.wait_for_load_state("networkidle")

    # Using POM
    homepage_overlay = HomepageOverlay(page=page)
    with page.expect_popup() as page1_info:
        # page.get_by_role("link", name="Apply for Value Package").click()
        homepage_overlay.apply_for_value_package_overlay_locator().click()
    page1 = page1_info.value
    page1.close()

    # Login page
    with page.expect_popup() as page2_info:
        page.get_by_role("link", name="Log In").click()
    page2 = page2_info.value
    # page2.get_by_placeholder("john.doe@gmail.com").click()
    # page2.get_by_placeholder("john.doe@gmail.com").fill("tito+mob01@expatrio.com", timeout=3000)
    # page2.get_by_placeholder("john.doe@gmail.com").press("Tab")
    # page2.get_by_label("Password", exact=True).fill("Bobon@mob01")
    # page2.get_by_role("button", name="Login", exact=True).click()
    # Using POM
    user_portal_login = UserPortalLoginPage(page=page2)
    user_portal_login.submit_login(email, password)

    # UP page
    # Adding waiting using while loop
    counter = 2
    overlay_not_visible = True
    while overlay_not_visible:
        # It will continue the if statement if .is_visible() return True
        if counter >= 0:
            if page2.is_visible("xpath=//p[@label='Maybe later']"):
                overlay_not_visible = False
            else:
                counter -= 1
        else:
            break

    # time.sleep(3)
    # a = page2.is_visible("xpath=//p[@label='Maybe later']")
    # print(a)
    page2.get_by_text("Maybe later").click()

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
        test_login(playwright)

