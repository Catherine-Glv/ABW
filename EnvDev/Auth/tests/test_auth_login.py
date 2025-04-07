import allure
import time
from EnvDev.Auth.locators.auth_locators import AuthLocators

@allure.feature("Проверка авторизации по номеру телефона")
class TestLogin:
    @allure.story("Проверка отображения попапа авторизации")
    def test_visible_auth_popup(self, auth_page):
        popup_window = AuthLocators.AUTH_POPUP_WINDOW
        auth_page.click_btn_login()
        time.sleep(5)
        assert auth_page.element_is_visible(popup_window) # 'Попап не отобразился'

    @allure.story("Проверка отображения инпута ввода номера телефона")
    def test_visible_tel_input(self, auth_page):
