import allure

from FinancePage.locators.page_locators import FinancePageLocators
from MainPage.locators.main_page_locators import MainPageLocators

@allure.feature("Проверка отображения элементов на странице")
class TestGoToFinance:
    @allure.story("Переход на страницу Финансы")
    def test_go_to_finance(self, main_page):
        main_page.click(locator=MainPageLocators.CLOSE_POPUP)
        """
        Тест: Проверка что кнопка в шапке ведет на корректный URL
        """
        expected_url = "https://abw.by/finance"

        main_page.open_page_finance()

        main_page.wait_for_url(expected_url)

        current_url = main_page.get_current_url()
        assert current_url == expected_url, \
            f"Ожидался URL: {expected_url}, получен: {current_url}"


class TestVisibleElements:
    @allure.story("Отображение заголовков")
    def test_titles_is_visible(self, finance_page):
        with (allure.step("Проверка основного заголовка")):
            assert finance_page.element_is_visible(locator=FinancePageLocators.TITLE_FINANCE)

        with (allure.step("Проверка подзаголовка")):
            assert finance_page.element_is_visible(locator=FinancePageLocators.SUBHEADING_FINANCE)

        with (allure.step("Проверка заголовка с расчетами лизингов")):
            assert finance_page.element_is_visible(locator=FinancePageLocators.TITLE_WITH_INFO)

    @allure.story("Отображение блока с фильтрами")
    def test_form_is_visible(self, finance_page):
        assert finance_page.element_is_visible(locator=FinancePageLocators.FORM_FINANCE)

    @allure.story("Отображение карточек лизингов")
    def test_cards_leasing_visible(self, finance_page):
        assert finance_page.element_is_visible(locator=FinancePageLocators.CARD_CONTENT)
        assert finance_page.element_is_visible(locator=FinancePageLocators.CARD_INFO)
        assert finance_page.element_is_visible(locator=FinancePageLocators.BUTTON_APPLICATION_ONE)

    def test_select_placeholder(self, finance_page):
        """Тест проверки плейсхолдера в селекте"""

        finance_page.verify_select_placeholder(
            selector="#city-select",
            expected_placeholder="Выберите город"
        )
