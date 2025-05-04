import pytest  
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  

@pytest.fixture(scope="function")  
def browser():  
    options = Options()  
    options.add_argument("--headless")  # Запуск без браузера (для CI)  
    driver = webdriver.Chrome(options=options)  
    yield driver  
    driver.quit()  
