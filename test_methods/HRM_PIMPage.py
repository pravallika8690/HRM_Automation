from test_methods.BasePage import BasePage

class PIMPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.pim_menu = "text=PIM"
        self.add_button = "button:has-text('Add')"
        self.first_name = "input[name='firstName']"
        self.last_name = "input[name='lastName']"
        self.save_button = "button[type='submit']"

        # ఈ మెథడ్ మీ PIM మెనూను క్లిక్ చేస్తుంది
    def navigate_to_pim(self):
            self.page.click(self.pim_menu)

    def add_new_employee(self, fname, lname):

        self.page.click(self.add_button)
        self.page.fill(self.first_name, fname)
        self.page.fill(self.last_name, lname)
        self.page.click(self.save_button)

    def search_employee(self, emp_name):
        self.page.click(self.pim_menu)  # లిస్ట్‌కి వెళ్లడానికి
        # ఎంప్లాయీ నేమ్ బాక్స్ అడ్రస్ (సాధారణంగా రెండవ ఇన్‌పుట్ బాక్స్)
        self.page.fill("form input[placeholder='Type for hints...']", emp_name)
        self.page.click("button[type='submit']")  # Search బటన్
        self.page.wait_for_load_state("networkidle")