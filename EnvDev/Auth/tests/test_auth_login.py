import allure
import time
from EnvDev.Auth.locators.auth_locators import AuthLocators
from EnvDev.Auth.tests.conftest import auth_page

@allure.feature("Проверка авторизации по номеру телефона")
class TestLogin:
    @allure.story("Проверка успешной авторизации")
    def test_successful_login(self, auth_page):
        with allure.step("Открытие попапа авторизации"):
            auth_page.click_btn_login()
            assert auth_page.auth_popup_is_visible(), 'Попап не отобразился'

        with allure.step("Ввод номера телефона"):
            auth_page.fill_tel_input()
            expected_tel_number = '+375000000000'
            actual_tel_number = auth_page.get_input_value(locator=AuthLocators.TEL_INPUT).replace(" ", "")
            assert expected_tel_number == actual_tel_number, (f'Номер не соответствует введенному, введен: '
                                                              f'{actual_tel_number}')

#assert auth_page.element_is_visible(locator=AuthLocators.HEADER_ICON_PROFILE), 'Авторизация не удалась'

    @allure.story("Проверка отображаемых элементов и текстов в попапе авторизации")
    def test_elements_visible(self, auth_page):
        with allure.step("Отображение поля для ввода телефона"):
            auth_page.click_btn_login()
            assert auth_page.tel_input_is_visible(), 'Поле телефона не отображается'

        with allure.step("Отображение плейсхолдера в инпуте телефона"):
            assert auth_page.element_is_visible(locator=AuthLocators.PLACEHOLDER_TEL_INPUT)

        with allure.step("Проверка текста в чек-боксе принятия условий"):
            expected_text_agree = auth_page.text_agree_checkbox
            actual_text_agree = auth_page.get_element_text(locator=AuthLocators.TEXT_AGREEMENT_CONDITION)
            assert expected_text_agree == actual_text_agree, (f'Текст принятия условий не соответствует, '
                                                              f'отображаемый текст: {actual_text_agree}')

        with allure.step("Проверка ссылок в принятии условий"):
            expected_url_terms_of_use = auth_page.url_terms_of_use
            expected_url_agreement_mail = auth_page.url_agreement_mail
            actual_url_terms_of_use = auth_page.get_attribute_href_url(locator=AuthLocators.TERMS_OF_USE)
            actual_url_agreement_mail = auth_page.get_attribute_href_url(locator=AuthLocators.AGREEMENT_MAIL)
            assert expected_url_terms_of_use == actual_url_terms_of_use, (f'Ссылка terms_of_use не соответствует или нет, вшитая '
                                                                          f'ссылка {actual_url_terms_of_use}')
            assert expected_url_agreement_mail == actual_url_agreement_mail, (f'Ссылка agreement_mail не соответствует или нет, вшитая '
                                                                          f'ссылка {actual_url_terms_of_use}')