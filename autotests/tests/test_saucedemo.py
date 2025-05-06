import allure
from autotests.pages.login_page import LoginPage
from autotests.pages.inventory_page import InventoryPage

@allure.feature("Saucedemo Tests")
class TestSaucedemo:
    @allure.story("Успешная авторизация")
    def test_successful_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page = InventoryPage(browser)
        assert inventory_page.is_opened()

    @allure.story("Добавление товара в корзину")
    def test_add_to_cart(self, browser):
        login_page = LoginPage(browser)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        inventory_page = InventoryPage(browser)
        inventory_page.add_first_item_to_cart()
        assert inventory_page.get_cart_count() == "1"
