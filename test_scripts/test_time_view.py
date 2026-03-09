import pytest
from test_methods.HRM_Loginpage import LoginPage
from test_methods.HRM_TimePage import TimePage


def test_view_employee_timesheet(page):
    login = LoginPage(page)
    time_mod = TimePage(page)

    # 1. Login
    page.goto("https://opensource-demo.orangehrmlive.com/")
    login.login_to_app("Admin", "admin123")

    # 2. Navigate and Search
    time_mod.navigate_to_time()
    # Using the name you provided
    time_mod.search_employee_timesheet("manda akhil user")

    # 3. Print Status
    page.wait_for_timeout(2000)
    status = time_mod.get_timesheet_status()
    print(f"\nTimesheet Status for Manda Akhil User: {status}")

    assert page.is_visible("text=Timesheet")