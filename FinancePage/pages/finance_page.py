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

    # def get_slider_value(self) -> int:
        # """Возвращает текущее значение ползунка (например 10)."""
        # return int(self.page.locator(FinancePageLocators.FIRST_PAYMENT_SLIDER).input_value())

    def get_label_value(self) -> int:
        """Возвращает значение процента над ползунком (например 10)."""
        return int(self.page.locator(FinancePageLocators.FIRST_PAYMENT_LABEL).first.inner_text())

    def get_container_percent(self) -> int:
        """
        Достаём процент из style:
        style="--3ef01c3c: linear-gradient(to right, var(--color-green-range) 25%, ...)"
        """
        style = self.page.locator(FinancePageLocators.FIRST_PAYMENT_CONTAINER).get_attribute("style")
        percent = int(style.split("var(--color-green-range)")[1].split("%")[0].strip())
        return percent

    def move_slider(self, value: int):
        """Передвигаем ползунок на нужное значение."""
        self.page.locator(FinancePageLocators.FIRST_PAYMENT_LABEL).fill(str(value))
