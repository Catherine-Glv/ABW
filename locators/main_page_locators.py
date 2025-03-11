class MainPageLocators:
    # Горячие предложения
    TITLE_HOT_OFFERS = "//h2[contains(text(),'Горячие предложения')]"
    BUTTON_HOT_OFFERS = "//button[contains(text(),'Хочу сюда')]"
    CARDS_HOT_OFFERS = "//div[@class='cards']"
    ONE_CARD_HOT_OFFERS = "(//a[@class='card'])[2]"
    HOVER_CARD_HOT_OFFERS = ("#__nuxt > div > div.application > div.app.wrapper-main.app-branding > div > main > "
                             "div.page-loader > div > div > div > div.container > div.cards > "
                             "a.card.card_hover.card > div")
    LARGE_CARDS_SELECTOR = "//a[@class='card card__large card']"
    TARGET_CARDS_SELECTOR = "//div[@class='target target_large']"
    SMALL_CARDS_SELECTOR = "//a[@class='card']"
