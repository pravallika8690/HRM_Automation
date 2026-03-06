import pytest
import json
from test_methods.HRM_Loginpage import LoginPage

# Load the data once
with open('config/test_data.json') as f:
    config_data = json.load(f)


@pytest.mark.parametrize("user_data", config_data['users'])
def test_orange_hrm_login(page, user_data):
    login_pg = LoginPage(page)

    # 1. Navigate
    page.goto(config_data['url'])

    # 2. Login using the current user from the list
    login_pg.login_to_app(user_data['username'], user_data['password'])

    # 3. Validation based on role
    if user_data['role'] == "Valid Admin":
        page.wait_for_selector("text=Dashboard", timeout=10000)
        assert page.is_visible("text=Dashboard")
    else:
        # 1. Wait for the error message to actually appear on the screen
        page.wait_for_selector(".oxd-alert-content-text", state="visible", timeout=5000)

        # 2. Now check if it is visible
        error_msg = page.locator(".oxd-alert-content-text")
        assert error_msg.is_visible()
        print(f"✅ Verified error message for: {user_data['username']}")
# Teardown: Close the page to clean up memory
    page.close()