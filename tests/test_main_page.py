import time
import allure

from locators.main_page_locators import MainPageLocators

@allure.feature('Проверка отображения блока "Горячие предложения"')
class TestHotOffers:
    @allure.story('Отображение контента блока')
    def test_hot_offers(self, main_page):
        with (allure.step('Проверка отображения заголовка в горячих предложениях')):
            assert main_page.element_is_visible(locator=MainPageLocators.TITLE_HOT_OFFERS), (f'Заголовок "Горячие '
                                                                                             f'предложения" '
                                                                                             f'не отобразился')

        with (allure.step('Проверка отображения кнопки Хочу сюда')):
            assert main_page.element_is_visible(locator=MainPageLocators.BUTTON_HOT_OFFERS), (f'Кнопка "Хочу сюда"'
                                                                                                  f'не отобразилась')

        with (allure.step('Проверка отображения карточек')):
            assert main_page.element_is_visible(locator=MainPageLocators.CARDS_HOT_OFFERS), (f'Карточки не '
                                                                                                 f'отображаются')

        with (allure.step('Проверка отображения ховера карточки')):
            main_page.hover_on_card()
            assert main_page.is_hover_visible(locator=MainPageLocators.HOVER_CARD_HOT_OFFERS), (f'Ховер у карточки '
                                                                                                f'не отображается')

@allure.feature('Проверка количества карточек')
class TestCountHotOffers:
    @allure.story('Пересчет карточек')
    def test_condition_1(self, cards_page):
        with (allure.step('Проверка кол-ва карточек в блоке, условие 1: нет больших карточек')):
            assert cards_page.check_condition_1(), "Условие 1 не выполнено"

    @allure.story('Пересчет карточек')
    def test_condition_2(self, cards_page):
        with (allure.step('Проверка кол-ва карточек в блоке, условие 2: 1 большая карточка, 10 маленьких')):
            assert cards_page.check_condition_2(), "Условие 2 не выполнено"
