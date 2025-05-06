from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest
import allure
from allure_commons.types import AttachmentType
import os

@pytest.fixture
def browser():
    # Устанавливаем правильный путь к chromedriver
    chromedriver_path = "/usr/local/bin/chromedriver"
    
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    service = Service(executable_path=chromedriver_path)
    
    try:
        driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )
        yield driver
    except Exception as e:
        allure.attach(
            str(e),
            name="browser_init_error",
            attachment_type=AttachmentType.TEXT
        )
        raise
    finally:
        if 'driver' in locals():
            if hasattr(pytest, 'test_failed') and pytest.test_failed:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=AttachmentType.PNG
                )
            driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(pytest, 'test_failed', rep.failed)
@pytest.fixture(autouse=True)

def add_allure_env(request, browser):
    allure.dynamic.link("https://www.saucedemo.com/")
    allure.dynamic.feature("UI Тесты")
    allure.dynamic.label("layer", "UI")
