import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected", [
    ("standard_user", "secret_sauce", True),
    ("locked_out_user", "secret_sauce", False),
    ("invalid", "invalid", False)
])
def test_login_with_params(browser, username, password, expected):
    login_page = LoginPage(browser)
    login_page.login(username, password)
    assert ("inventory.html" in browser.current_url) == expected

