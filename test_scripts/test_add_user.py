import pytest
from test_methods.HRM_Loginpage import LoginPage
from test_methods.HRM_AdminPage import AdminPage


def test_add_new_admin_user(page):
    # Initialize Page Objects
    login = LoginPage(page)
    admin = AdminPage(page)

    # Define variables locally to avoid NameErrors
    new_username = "Midhunam_User"

    # 1. Login
    page.goto("https://opensource-demo.orangehrmlive.com/")
    login.login_to_app("Admin", "admin123")

    # 2. Add User
    # Ensure 'Midhunam Cafe' matches an existing employee in your OrangeHRM instance
    admin.navigate_to_admin()
    admin.add_new_user("manda akhil user", new_username, "Password@123")

    # 3. Assertion (Reliable Logic)
    # Explicitly navigate to the user list to refresh the view
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

    # Filter for the newly created user
    page.get_by_role("textbox").nth(1).fill(new_username)
    page.get_by_role("button", name="Search").click()

    # Wait for the search result to populate the table
    page.wait_for_timeout(3000)
    assert page.is_visible(f"text={new_username}"), f"User {new_username} was not found in the search results."