import pytest
from playwright.sync_api import sync_playwright
from FinancePage.pages.main_page import MainPage


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
def main_page(page):
    MainPage(page).open_page()
    return MainPage(page)