from MainPage.locators.main_page_locators import MainPageLocators
from MainPage.pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://test.abw.by/"

    def open_page(self, url=URL) -> None:
        self.open_url(url=url)

    def click_btn_hot_offers(self) -> None:
        self.click(locator=MainPageLocators.BUTTON_HOT_OFFERS)

    def click_card_hot_offers(self) -> None:
        self.click(locator=MainPageLocators.ONE_CARD_HOT_OFFERS)

    def hover_on_card(self) -> None:
        # Наведение на карточку
        self.hover_element(locator=MainPageLocators.ONE_CARD_HOT_OFFERS)

class CardsPage(BasePage):
    large_cards_selector = MainPageLocators.LARGE_CARDS_SELECTOR
    small_cards_selector = MainPageLocators.SMALL_CARDS_SELECTOR
    target_large_selector = MainPageLocators.TARGET_CARDS_SELECTOR

    URL = "https://abw.by/"

    def open_page(self, url=URL) -> None:
        self.open_url(url=url)

    def count_large_cards(self) -> int:
        """
        Возвращает количество больших карточек.
        """
        return self.page.locator(self.large_cards_selector).count()

    def count_small_cards(self) -> int:
        """
        Возвращает количество маленьких карточек.
        """
        return self.page.locator(self.small_cards_selector).count()

    def is_target_large_visible(self) -> bool:
        """
        Проверяет, отображается ли карточка target_large.
        """
        return self.page.locator(self.target_large_selector).is_visible()

    def check_condition_1(self) -> bool:
        """
        Проверка условия 1:
        - Нет больших карточек.
        - 14 маленьких карточек.
        - target_large отображается.
        """
        return (
            self.count_large_cards() == 0
            and self.count_small_cards() == 14
            and self.is_target_large_visible()
        )

    def check_condition_2(self) -> bool:
        """
        Проверка условия 2:
        - 1 большая карточка.
        - 10 маленьких карточек.
        - target_large отображается.
        """
        return (
            self.count_large_cards() == 1
            and self.count_small_cards() == 10
            and self.is_target_large_visible()
        )

    def check_condition_3(self) -> bool:
        """
        Проверка условия 3:
        - 2 большие карточки.
        - 6 маленьких карточек.
        - target_large отображается.
        """
        return (
            self.count_large_cards() == 2
            and self.count_small_cards() == 6
            and self.is_target_large_visible()
        )

    def check_condition_4(self) -> bool:
        """
        Проверка условия 4:
        - 3 большие карточки.
        - 6 маленьких карточек.
        - target_large НЕ отображается.
        """
        return (
            self.count_large_cards() == 3
            and self.count_small_cards() == 6
            and not self.is_target_large_visible()
        )

    def check_condition_5(self) -> bool:
        """
        Проверка условия 5:
        - 4 или 5 больших карточек.
        - 4 маленькие карточки.
        - target_large отображается.
        """
        return (
            self.count_large_cards() in [4, 5]
            and self.count_small_cards() == 4
            and self.is_target_large_visible()
        )

    def check_condition_6(self) -> bool:
        """
        Проверка условия 6:
        - 6 больших карточек.
        - Маленькие карточки НЕ отображаются.
        - target_large НЕ отображается.
        """
        return (
            self.count_large_cards() == 6
            and self.count_small_cards() == 0
            and not self.is_target_large_visible()
        )