import time

from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str) -> None:
        self.page.goto(url=url)

    def click(self, locator: str) -> None:
        element = self.page.wait_for_selector(selector=locator)
        element.click()

    def hover_element(self, locator: str) -> None:
        # Наведение на элемент
        element = self.page.locator(selector=locator)
        element.hover()

    def is_hover_visible(self, locator: str) -> bool:
        # Отображение ховера
        hover_element = self.page.locator(selector=locator)
        return hover_element.is_visible()
        # if self.page.is_visible(selector=locator, timeout=10):
        #     return True
        # else:
        #     raise Exception('Элемент не отобразился на странице')

    def fill_value(self, locator: str, value: str) -> None:
        self.page.wait_for_selector(selector=locator)
        self.page.fill(selector=locator, value=value)

    def select_element(self, locator: str, label: str) -> bool:
        if self.page.select_option(locator, label=label):
            return True
        else:
            raise Exception('Элемент не выбран')

    def get_element_text(self, locator: str) -> str:
        return self.page.inner_text(selector=locator)

    def get_current_url(self) -> str:
        return self.page.url

    def get_elements(self, locator) -> list:
        return self.page.query_selector_all(selector=locator)

    def element_is_visible(self, locator: str) -> bool:
        if self.page.is_visible(selector=locator):
            return True
        else:
            raise Exception('Элемент не отобразился на странице')