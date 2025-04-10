import pytest
from playwright.sync_api import sync_playwright
from EnvDev.Auth.pages.auth_page_tel import AuthPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def auth_page(page):
    AuthPage(page).open_page()
    return AuthPage(page)
