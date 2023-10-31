class Homepage:
    def __init__(self, page):
        self.page = page

    def navigate_to_homepage(self):
        return self.page.goto("https://www.expatrio.com/")

    def accept_all_cookies_locator(self):
        return self.page.get_by_role("button", name="Accept all")

