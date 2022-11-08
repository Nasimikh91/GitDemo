from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TradePage:
    def __init__(self, driver):
        self.driver = driver

    trade_button = (By.XPATH, "//button[@data-testid='trade-page-button']")
    symbol = (By.ID, "navigation-symbol-search")
    symbol_lookup = (By.XPATH, "//span[text()='TRADEWEB MARKETS INC COM CL A']")
    side = (By.XPATH, "//button[@direction='buy']")
    quantity = (By.XPATH, "//input[@type='number']")
    review_order = (By.CSS_SELECTOR, "#review-order-button")
    send_order = (By.CSS_SELECTOR, "#send-order-button")
    notification = (By.XPATH, "//div[text()= 'Notifications']")
    original_notification = (By.XPATH, "(//div[@class='NotificationCardstyled__Text-liTWMR fhanmg'])[1]")

    def get_trade_button(self):
        return self.driver.find_element(*TradePage.trade_button)

    def get_symbol(self):
        return self.driver.find_element(*TradePage.symbol)

    def get_symbol_lookup(self):
        return self.driver.find_element(*TradePage.symbol_lookup)

    def get_side(self):
        return self.driver.find_element(*TradePage.side)

    def get_quantity(self):
        return self.driver.find_element(*TradePage.quantity)

    def get_quantity_input(self):
        return self.driver.find_element(*TradePage.quantity)

    def get_review_order(self):
        return self.driver.find_element(*TradePage.review_order)

    def get_send_order(self):
        return self.driver.find_element(*TradePage.send_order)

    def get_notification(self):
        return self.driver.find_element(*TradePage.notification)

    def get_order_confirmation(self):
        original_confirmation = []
        original_message = [
            self.driver.find_element(*TradePage.original_notification).text]
        for records in original_message:
            original_confirmation.append(records)
        assert original_message == original_confirmation
        return original_message
