class TimePage:
    def __init__(self, page):
        self.page = page
        self.time_menu = "text=Time"
        self.employee_name_input = "input[placeholder='Type for hints...']"
        self.view_button = "button[type='submit']"
        self.status_text = ".orangehrm-timesheet-footer--stats" # Adjust based on UI

    def navigate_to_time(self):
        self.page.click(self.time_menu)

    def search_employee_timesheet(self, emp_name):
        # Type the name and wait for the dropdown hint
        self.page.fill(self.employee_name_input, emp_name)
        self.page.wait_for_selector(".oxd-autocomplete-dropdown")
        # Click the first matching option in the dropdown
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.page.click(self.view_button)

    def get_timesheet_status(self):
        # Returns the status text (e.g., 'Status: Submitted')
        return self.page.locator(self.status_text).first.inner_text()