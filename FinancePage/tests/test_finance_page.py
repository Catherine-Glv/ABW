import allure
import pytest

from FinancePage.locators.page_locators import FinancePageLocators
from MainPage.locators.main_page_locators import MainPageLocators


@allure.feature("Проверка отображения элементов на странице")
class TestGoToFinance:
    @allure.story("Переход на страницу Финансы")
    def test_go_to_finance(self, main_page):
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

    @allure.story("Отображение плейсхолдеров в селектах фильтра")
    @pytest.mark.parametrize("expected_text", ["Марка"])
    def test_select_mark(self, finance_page, expected_text):
        with (allure.step("Проверка плейсхолдера селекта 'Марка'")):
            assert finance_page.element_is_visible(locator=FinancePageLocators.BUTTON_MARK), (
                f"Селект 'Марка' должен быть видимым")
            assert finance_page.get_element_text(locator=FinancePageLocators.BUTTON_MARK) == expected_text, (
                f"Текст плейсхолдера не совпадает")

    @pytest.mark.parametrize("expected_text", ["Модель"])
    def test_select_model(self, finance_page, expected_text):
        with (allure.step("Проверка плейсхолдера селекта 'Модель'")):
            assert finance_page.element_is_visible(locator=FinancePageLocators.BUTTON_MODEL), (
                f"Селект 'Модель' должен быть видимым")
            assert finance_page.get_element_text(locator=FinancePageLocators.BUTTON_MODEL) == expected_text, (
                f"Текст плейсхолдера не совпадает")

    @pytest.mark.parametrize("expected_text", ["2025\nГод"])
    def test_select_year(self, finance_page, expected_text):
        with (allure.step("Проверка плейсхолдера селекта '2025\nГод'")):
            assert finance_page.element_is_visible(locator=FinancePageLocators.BUTTON_YEAR), (
                f"Селект 'Год' должен быть видимым")
            assert finance_page.get_element_text(locator=FinancePageLocators.BUTTON_YEAR) == expected_text, (
                f"Текст плейсхолдера не совпадает")

    # def test_banner_is_visible(self, finance_page):
    #     assert finance_page.element_is_visible(locator=FinancePageLocators.BANNER), "Баннер не отображается"

class TestFilters:
    @allure.story("Работа селектов")
    def test_choice_select(self, finance_page):
        ...

