import pytest  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  
import allure

@pytest.fixture
def attach_screenshot(browser):
    yield
    allure.attach(
        browser.get_screenshot_as_png(),
        name="screenshot",
        attachment_type=allure.attachment_type.PNG
    )

@pytest.fixture(scope="function")  
def browser():  
    options = Options()  
    options.add_argument("--headless")  # Запуск без браузера (для CI)  
    driver = webdriver.Chrome(options=options)  
    yield driver  
    driver.quit()  
