class UserPortalLoginPage:
    def __init__(self, page):
        self.page = page

    def submit_login(self, email: str, password: str):
        self.page.get_by_placeholder("john.doe@gmail.com").click()
        self.page.get_by_placeholder("john.doe@gmail.com").fill(email, timeout=3000)
        self.page.get_by_placeholder("john.doe@gmail.com").press("Tab")
        self.page.get_by_label("Password", exact=True).fill(password)
        self.page.get_by_role("button", name="Login", exact=True).click()
