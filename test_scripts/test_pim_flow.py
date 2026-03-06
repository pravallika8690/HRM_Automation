import pytest
from config.config import TestData  # Importing our new config class
from test_methods.HRM_Loginpage import LoginPage
from test_methods.HRM_PIMPage import PIMPage


def test_add_new_employee_flow(page):
    # 1. Initialize Page Objects
    login_pg = LoginPage(page)
    pim_pg = PIMPage(page)

    # 2. Login Action using Config constants
    page.goto(TestData.BASE_URL, timeout=60000)
    login_pg.login_to_app(TestData.ADMIN_USER, TestData.ADMIN_PASS)

    # 3. PIM Action
    pim_pg.navigate_to_pim()
    pim_pg.add_new_employee(TestData.FIRST_NAME, TestData.LAST_NAME)

    # 4. Search and Verify
    pim_pg.search_employee(TestData.FIRST_NAME)
    page.wait_for_selector(f"text={TestData.FIRST_NAME}", timeout=20000)
    assert page.is_visible(f"text={TestData.FIRST_NAME}")

    # 5. Logout
    login_pg.logout_from_app()
    page.close()