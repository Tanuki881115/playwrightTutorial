class HomepageOverlay:
    def __init__(self, page):
        self.page = page

    def apply_for_value_package_overlay_locator(self):
        return self.page.get_by_role("link", name="Apply for Value Package")