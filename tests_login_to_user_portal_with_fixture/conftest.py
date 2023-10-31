from playwright.sync_api import Playwright
import pytest
from pom.homepage_main import Homepage
from pom.homepage_overlay import HomepageOverlay


"""
For the scope of the fixture.
'session' scope will take the test much faster then 'function'.
The reason is for 'session' scope with example like login to user portal,
for each test case, we will just launch one session
then based on how many test case that we have
all of test will use the same session and at the end of the last test, it will do the tear down.

If we use it with function scope, for each test case, it will run the 1st test then do tear down.
On the next test, it will open new session and run the test case and tear down.
Repeating this process over and over will take lots of time.
Especially if we have lots of test case to cover.

 
"""


@pytest.fixture()
def setup(page):
    """
    Playwright already made a ready-made fixture called page.
    By inheriting it from 'page' in our 'setup' function
    Instead of passing setup(playwright: Playwright) on the function,
    we can set it up as setup(page).
    Therefore, we do not need the following block of code:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

    Things to remember when we use the ready-made fixture from playwright,
    it will run on playwright default settings e.g.: headless mode
    BUT we can still set some options using CLI

    If we set up the test using fixture do not mixed it up with other test
    That is not implemented using fixture
    It will fail those tests

    NOTE:
        'page' is only working for fixture with scope=function.
        If we try to user page in session scope, it is gonna failing
    """

    # Initializing Homepage class
    homepage = Homepage(page=page)

    # Using POM to navigate to Homepage
    homepage.navigate_to_homepage()

    # Do not user set_default_timeout() when it is not necessary
    # The reason is playwright by default when locating element already have this waiting
    # If a web element will show after 5 seconds but we set set_default_timeout() for 3 seconds
    # It will fail the test
    # page.set_default_timeout(3000)

    yield page

    # When using fixture, we need to set up the teardown
    # Especially if we run it on scope level function
    page.close()


@pytest.fixture()
def login_setup(setup):
    """
    We can set another fixture and inherit it from another fixture

    If we want to do a fixture like this, make sure that we don't yield several variable that should be used
    on the test case
    For example:
    in this fixture, we 'yield' page at the end.
    But before yield, we also have page1 and page2.
    Since page2 is being used on the test case, it is not gonna work.
    """

    page = setup

    # Initializing Homepage class
    homepage = Homepage(page=page)

    # Using POM to navigate to Homepage
    # page.goto("https://www.expatrio.com/")
    homepage.navigate_to_homepage()

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
    page2.get_by_placeholder("john.doe@gmail.com").click()
    page2.get_by_placeholder("john.doe@gmail.com").fill("tito+mob01@expatrio.com", timeout=3000)
    page2.get_by_placeholder("john.doe@gmail.com").press("Tab")
    page2.get_by_label("Password", exact=True).fill("Bobon@mob01")
    page2.get_by_role("button", name="Login", exact=True).click()

    # UP page
    # Adding waiting using while loop
    overlay_not_visible = True
    while overlay_not_visible:
        # It will continue the if statement if .is_visible() return True
        if page2.is_visible("xpath=//p[@label='Maybe later']"):
            overlay_not_visible = False

    page2.get_by_text("Maybe later").click()

    yield page
