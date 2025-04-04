from playwright.sync_api import Page, expect, TimeoutError

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_url(self, url: str) -> None:
        self.page.goto(url=url)

    def click(self, locator: str) -> None:
        element = self.page.wait_for_selector(selector=locator)
        element.click()

    def fill_value(self, locator: str, value: str) -> None:
        self.page.wait_for_selector(selector=locator)
        self.page.fill(selector=locator, value=value)

    def get_element_text(self, locator: str) -> str:
        return self.page.inner_text(selector=locator)

    def is_button_clickable(self, locator: str, timeout: float = 1.0) -> bool:
        try:
            # Проверяем, что элемент видим, enabled и не имеет атрибута 'disabled'
            expect(self.page.is_visible(selector=locator, timeout=timeout * 1000))
            expect(self.page.is_enabled(selector=locator, timeout=timeout * 1000))
            return True
        except (TimeoutError, AssertionError):
            return False

    def element_is_visible(self, locator: str) -> bool:
        if self.page.is_visible(selector=locator):
            return True
        else:
            raise Exception('Элемент не отобразился на странице')