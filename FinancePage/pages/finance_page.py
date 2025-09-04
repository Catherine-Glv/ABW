from playwright.sync_api import Page, expect
from FinancePage.locators.page_locators import FinancePageLocators
from FinancePage.pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://abw.by/"

    def open_page(self, url=URL) -> None:
        self.open_url(url=url)

    def open_page_finance(self) -> None:
        self.click(locator=FinancePageLocators.HEADER_BUTTON)

    def get_header_button_url(self) -> str:
        """
        Получает URL из атрибута href кнопки в шапке
        (прямое обращение к page.locator)
        """
        return self.page.locator(FinancePageLocators.HEADER_BUTTON).get_attribute("href")

    def wait_for_url(self, url: str, timeout: int = 5000) -> None:
        self.page.wait_for_url(url, timeout=timeout)


class FinancePage(BasePage):
    URL = "https://abw.by/finance"

    def open_page(self, url=URL) -> None:
        self.open_url(url=url)

    # def has_placeholder(self, locator: str, expected: str) -> bool:
    #     """Проверка текста плейсхолдера"""
    #     return self.page.inner_text() == expected


