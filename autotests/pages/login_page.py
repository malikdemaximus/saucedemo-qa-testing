from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container")

    def login(self, username, password):
        self.find_element(self.USERNAME_INPUT).send_keys(username)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
