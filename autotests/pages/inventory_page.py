from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@id,'add-to-cart')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def is_opened(self):
        return "inventory" in self.driver.current_url

    def add_first_item_to_cart(self):
        self.find_elements(self.ADD_TO_CART_BUTTON)[0].click()

    def get_cart_count(self):
        return self.find_element(self.CART_BADGE).text
