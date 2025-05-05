from pages.login_page import LoginPage

def test_successful_login(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in browser.current_url
    
def test_invalid_login(browser):  
    browser.get("https://www.saucedemo.com/")  
    browser.find_element("id", "user-name").send_keys("locked_out_user")  
    browser.find_element("id", "password").send_keys("wrong_pass")  
    browser.find_element("id", "login-button").click()  
    error = browser.find_element("css selector", ".error-message-container").text  
    assert "Epic sadface" in error, "Error message not found!"  
