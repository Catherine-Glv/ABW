from EnvDev.Auth.locators.auth_locators import AuthLocators
from EnvDev.Auth.pages.base_page import BasePage
from playwright.sync_api import Page, expect

class AuthPage(BasePage):
    URL = "https://test.abw.by/"
    text_agree_checkbox = ("При Регистрации или Авторизации на сайте ABW.BY, Вы соглашаетесь на рассылку с"
                           " рекомендациями, новостями и специальными предложениями от ABW.BY. Если вы не хотите"
                           " получать такие письма, вы можете отключить рассылку личном кабинете. Подробности о "
                           "рассылках и их условиях — в Соглашении на обработку персональных данных и получении "
                           "рассылки рекламного характера.")
    url_terms_of_use = "/terms-of-use"
    url_agreement_mail = "/agreement-mail"

    def open_page(self, url=URL) -> None:
        self.open_url(url=url)

    def login(self) -> None:
            self.click_btn_login()
            self.fill_tel_input()
            self.click_agree_checkbox()
            self.click_next_button()
            # Проверка с явным ожиданием (до 10 секунд)
            try:
                if self.page.locator(AuthLocators.CAPTCHA_IFRAME).is_visible(timeout=10000):
                    self.click_captcha()
            except:
                pass  # Капча не появилась за отведенное время

            self.fill_code()

    def click_btn_login(self) -> None:
        self.click(locator=AuthLocators.LOGIN_BUTTON)

    def fill_tel_input(self) -> None:
        self.fill_value(locator=AuthLocators.TEL_INPUT, value='000000000')

    def click_agree_checkbox(self):
        self.click_checkbox(locator=AuthLocators.AGREE_CHECKBOX)

    def button_is_enabled(self):
        self.is_button_clickable(locator=AuthLocators.NEXT_BUTTON)

    def click_next_button(self):
        self.click(locator=AuthLocators.NEXT_BUTTON)

    def click_captcha(self):
        self.click(locator=AuthLocators.CAPTCHA_IFRAME)

    def checking_captcha(self):
        try:
            if self.page.locator(AuthLocators.CAPTCHA_IFRAME).is_visible(timeout=10000):
                self.click_captcha()
        except:
            pass  # Капча не появилась за отведенное время

    def fill_code(self):
        self.fill_value(locator=AuthLocators.SMS_CODE_INPUT_1, value='9')
        self.fill_value(locator=AuthLocators.SMS_CODE_INPUT_2, value='6')
        self.fill_value(locator=AuthLocators.SMS_CODE_INPUT_3, value='9')
        self.fill_value(locator=AuthLocators.SMS_CODE_INPUT_4, value='5')

    # def click_sms_login(self):
    #     self.click(locator=AuthLocators.SMS_NEXT_BUTTON)

    def auth_popup_is_visible(self) -> bool:
        try:
            self.element_is_visible(locator=AuthLocators.AUTH_POPUP_WINDOW)
            return True
        except Exception:
            return False

    def tel_input_is_visible(self) -> bool:
        try:
            self.element_is_visible(locator=AuthLocators.TEL_INPUT)
            return True
        except Exception:
            return False