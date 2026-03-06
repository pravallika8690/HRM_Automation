import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page():
    # Setup: బ్రౌజర్ స్టార్ట్ చేయడం
    with sync_playwright() as p:
        # 'headed=True' ని తీసేసి 'headless=False' అని పెట్టండి
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page  # ఇక్కడ టెస్ట్ రన్ అవుతుంది

        # Teardown: టెస్ట్ అయిపోగానే క్లోజ్ చేయడం
        page.close()
        context.close()
        browser.close()