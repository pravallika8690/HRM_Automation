class RecruitmentPage:
    def __init__(self, page):
        self.page = page
        self.recruitment_menu = "text=Recruitment"
        self.first_checkbox = ".oxd-table-card .oxd-checkbox-wrapper >> nth=0"
        self.delete_icon = ".oxd-icon.bi-trash >> nth=0"
        self.confirm_delete_button = "button:has-text('Yes, Delete')"

    def navigate_to_recruitment(self):
        self.page.click(self.recruitment_menu)

    def select_first_candidate_and_delete(self):
        # 1. Select the checkbox
        self.page.click(self.first_checkbox)
        # 2. Click the trash/delete icon
        self.page.click(self.delete_icon)
        # 3. Click the 'Yes, Delete' confirmation button
        self.page.click(self.confirm_delete_button)