# test_scripts/test_add_user.py
import pytest
from test_methods.HRM_Loginpage import LoginPage
from test_methods.HRM_AdminPage import AdminPage

def test_add_new_admin_user(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    # 1. Login
    page.goto("https://opensource-demo.orangehrmlive.com/")
    login.login_to_app("Admin", "admin123")

    # 2. Add User
    admin.navigate_to_admin()
    # Note: Use a valid employee name existing in your demo instance
    admin.add_new_user("Midhunam Cafe", "Midhunam_User", "Password@123")

    # 3. Assertion (Reliable Search Logic)
    # Navigate to the user list to ensure a clean state
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

    # Fill the username in the search box (index 1 is typically the Username field)
    page.get_by_role("textbox").nth(1).fill("Midhunam_User")
    page.get_by_role("button", name="Search").click()

    # Wait for the network to be idle to ensure the table has refreshed
    page.wait_for_load_state("networkidle")

    # Use a more specific locator to wait for the user to appear in the table
    page.wait_for_selector("//div[@role='table']//div[contains(text(),'Midhunam_User')]", timeout=10000)
    assert page.is_visible("text=Midhunam_User")