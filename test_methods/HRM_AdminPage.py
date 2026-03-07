from test_methods.BasePage import BasePage


# test_methods/HRM_AdminPage.py
class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_menu = "text=Admin"
        self.add_button = "button:has-text('Add')"
        self.user_role_dropdown = ".oxd-select-text >> nth=0"
        self.employee_name_input = "input[placeholder='Type for hints...']"
        self.username_input = "xpath=(//input[@class='oxd-input oxd-input--active'])[2]"
        self.password_input = "xpath=(//input[@type='password'])[1]"
        self.confirm_password_input = "xpath=(//input[@type='password'])[2]"
        self.save_button = "button[type='submit']"

    def navigate_to_admin(self):
        self.page.click(self.admin_menu)

    def add_new_user(self, emp_name, new_username, new_password):
        self.page.click(self.add_button)
        # Selecting User Role as 'ESS'
        self.page.click(self.user_role_dropdown)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        # Filling details
        self.page.fill(self.employee_name_input, emp_name)
        self.page.wait_for_selector(".oxd-autocomplete-dropdown")  # Wait for hints
        self.page.keyboard.press("Enter")

        self.page.fill(self.username_input, new_username)
        self.page.fill(self.password_input, new_password)
        self.page.fill(self.confirm_password_input, new_password)
        self.page.click(self.save_button)