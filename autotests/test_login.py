def test_successful_login(browser):  
    browser.get("https://www.saucedemo.com/")  
    browser.find_element("id", "user-name").send_keys("standard_user")  
    browser.find_element("id", "password").send_keys("secret_sauce")  
    browser.find_element("id", "login-button").click()  
    assert "inventory.html" in browser.current_url, "Login failed!"  

def test_invalid_login(browser):  
    browser.get("https://www.saucedemo.com/")  
    browser.find_element("id", "user-name").send_keys("locked_out_user")  
    browser.find_element("id", "password").send_keys("wrong_pass")  
    browser.find_element("id", "login-button").click()  
    error = browser.find_element("css selector", ".error-message-container").text  
    assert "Epic sadface" in error, "Error message not found!"  
