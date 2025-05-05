from pages.login_page import LoginPage

def test_successful_login(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in browser.current_url
