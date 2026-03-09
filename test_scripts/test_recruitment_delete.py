import pytest
import os
from test_methods.HRM_Loginpage import LoginPage
from test_methods.HRM_RecruitmentPage import RecruitmentPage


def test_delete_recruitment_candidate(page):
    login = LoginPage(page)
    recruitment = RecruitmentPage(page)

    # 1. Login to OrangeHRM
    page.goto("https://opensource-demo.orangehrmlive.com/")
    login.login_to_app("Admin", "admin123")

    # 2. Navigate and Perform Deletion
    recruitment.navigate_to_recruitment()

    # Take screenshot BEFORE deletion for records
    page.screenshot(path="test_reports/screenshots/before_delete.png")

    recruitment.select_first_candidate_and_delete()

    # 3. Take screenshot DURING/AFTER deletion
    if not os.path.exists("test_reports/screenshots"):
        os.makedirs("test_reports/screenshots")
    page.screenshot(path="test_reports/screenshots/after_delete.png")

    # 4. Verify Success Message
    # OrangeHRM shows a 'Successfully Deleted' toast
    success_message = page.wait_for_selector("text=Successfully Deleted", timeout=5000)

    if success_message:
        print("\nOUTPUT: Candidate successfully deleted")

    assert page.is_visible("text=Successfully Deleted")