from FinancePage.pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://abw.by/finance"

    def open_page(self, url=URL) -> None:
        self.open_url(url=url)