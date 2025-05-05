from .base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    
    def get_items_count(self):
        return len(self.find_elements(self.ITEM_NAMES))
