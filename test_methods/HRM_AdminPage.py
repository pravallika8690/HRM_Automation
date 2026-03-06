from test_methods.BasePage import BasePage

class AdminPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators for Admin Page
        self.admin_menu = "text=Admin"
        self.add_button = "button:has-text('Add')"

    def navigate_to_admin(self):
        self.page.click(self.admin_menu)