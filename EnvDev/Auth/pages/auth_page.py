from EnvDev.Auth.locators.auth_locators import AuthLocators
from EnvDev.Auth.pages.base_page import BasePage


class AuthPage(BasePage):
    URL = "https://test.abw.by/"

    def open_page(self, url=URL) -> None:
        self.open_url(url=url)

    def click_btn_login(self) -> None:
        self.click(locator=AuthLocators.LOGIN_BUTTON)

    def fill_tel_input(self) -> None:
        self.fill_value(locator=AuthLocators.TEL_INPUT, value='298489123')

    def click_agree_checkbox(self):
        self.click(locator=AuthLocators.AGREE_CHECKBOX)

    def button_is_enabled(self):
        self.is_button_clickable(locator=AuthLocators.NEXT_BUTTON)

    def click_next_button(self):
        self.click(locator=AuthLocators.NEXT_BUTTON)

    def click_captcha(self):
        self.click(locator=AuthLocators.CAPTCHA_IFRAME)

    def fill_code(self):
        self.fill_value(locator=AuthLocators.SMS_CODE_INPUT_1, value='9')
        self.fill_value(locator=AuthLocators.SMS_CODE_INPUT_2, value='6')
        self.fill_value(locator=AuthLocators.SMS_CODE_INPUT_3, value='9')
        self.fill_value(locator=AuthLocators.SMS_CODE_INPUT_4, value='5')

    def click_sms_login(self):
        self.click(locator=AuthLocators.SMS_NEXT_BUTTON)