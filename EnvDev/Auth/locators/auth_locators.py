class AuthLocators:
    LOGIN_BUTTON = ("//button[contains(text(),'Войти')]")
    AUTH_POPUP_WINDOW = "//div[@class='modal-content modal-content--open']"
    AUTH_TITLE_IN_POPUP = "//p[@class='auth__title']"
    HEADER_ICON_PROFILE = "//button[@class='header-desktop__profile']"

class AuthLocatorsTel:
    AGREE_CHECKBOX = "//label[@class='agreement__label']"
    INPUT_CHECKBOX = "//input[@type='checkbox']"
    TEL_INPUT = "//input[@placeholder='Введите номер телефона']"
    PLACEHOLDER_TEL_INPUT = "//span[@class='_placeholder_jgnm1_57 _placeholderActive_jgnm1_71']"
    TEXT_AGREEMENT_CONDITION = "//span[@class='agreement__condition']"
    TERMS_OF_USE = "//a[contains(text(),'Соглашении на обработку персональных данных')]"
    AGREEMENT_MAIL = "//a[contains(text(),'получении рассылки рекламного характера.')]"
    NEXT_BUTTON = "//button[contains(text(),'Далее')]"
    CAPTCHA_IFRAME = "//iframe[@title='reCAPTCHA']"
    INPUT_CODE = "//div[@class='otp-container']"
    TITLE_PHONE = "//p[@class='frame__title frame__title--phone']"
    SMS_CODE_INPUT_1 = ("body > div.modal-overlay > div > div > div > form > div > div.frame-code-container > "
                        "div > input:nth-child(1)")
    SMS_CODE_INPUT_2 = ("body > div.modal-overlay > div > div > div > form > div > div.frame-code-container > "
                        "div > input:nth-child(2)")
    SMS_CODE_INPUT_3 = ("body > div.modal-overlay > div > div > div > form > div > div.frame-code-container > "
                        "div > input:nth-child(3)")
    SMS_CODE_INPUT_4 = ("body > div.modal-overlay > div > div > div > form > div > div.frame-code-container > "
                        "div > input:nth-child(4)")
    # SMS_NEXT_BUTTON = "//button[contains(text(),'Отправить')]"
    RESEND_CODE = "//button[contains(text(),'Выслать код повторно')]"
    BUTTON_RESET_PHONE = "//button[contains(text(),'Неверный номер. Изменить')]"

class AuthLocatorsUr:
    BUTTON_UR_LOGIN = "//button[contains(text(),'Вход для юридических лиц')]"
    TITLE_POPUP_UR = "//span[contains(text(),'Вход для юридических лиц')]"
    INPUT_LOGIN = "//input[@placeholder='Логин']"
    INPUT_PASSWORD = "//input[@placeholder='Пароль']"
    AGREE_CHECKBOX = "//label[@class='agreement__label']"
    INPUT_CHECKBOX = "//input[@type='checkbox']"
    TEXT_AGREEMENT_CONDITION = "//span[@class='agreement__condition']"
    TERMS_OF_USE = "//a[contains(text(),'Соглашении на обработку персональных данных')]"
    AGREEMENT_MAIL = "//a[contains(text(),'получении рассылки рекламного характера.')]"
    NEXT_BUTTON = "//button[contains(text(),'Далее')]"
