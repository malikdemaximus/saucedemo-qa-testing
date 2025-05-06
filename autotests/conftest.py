from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest
import allure
from allure_commons.types import AttachmentType
import os

from selenium.common.exceptions import WebDriverException

@pytest.fixture
def browser():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")  # Новый headless-режим
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(options=chrome_options)
        yield driver
    except WebDriverException as e:
        pytest.fail(f"Browser initialization failed: {str(e)}")
    finally:
        if 'driver' in locals():
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
