from playwright.sync_api import expect
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
        """
        Ожидает перехода на указанный URL

        Args:
            url: ожидаемый URL
            timeout: таймаут в миллисекундах
        """
        self.page.wait_for_url(url, timeout=timeout)


class FinancePage(BasePage):
    URL = "https://abw.by/finance"

    def open_page(self, url=URL) -> None:
        self.open_url(url=url)

    def verify_select_placeholder(self, selector: str, expected_placeholder: str):
        """
        Проверяет плейсхолдер с использованием Playwright expect

        Args:
            selector: CSS селектор элемента
            expected_placeholder: ожидаемый текст плейсхолдера
        """
        select_locator = self.page.locator(selector)
        expect(select_locator).to_have_attribute("placeholder", expected_placeholder)

    # def get_select_placeholder(self, selector: str) -> str:
    #     """
    #     Получает текст плейсхолдера селекта
    #
    #     Args:
    #         selector: CSS селектор элемента
    #
    #     Returns:
    #         str: текст плейсхолдера
    #     """
    #     return self.page.locator(selector).get_attribute("placeholder")