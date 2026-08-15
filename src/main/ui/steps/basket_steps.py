import allure
from src.main.ui.pages.basket_page import BasketPage
from playwright.sync_api import Page


class BasketSteps:
    def __init__(self, page: Page):
        self.page = page
        self.basket_page = BasketPage(page)

    @allure.step("Переход в корзину")
    def open_cart(self):
        return self.basket_page.open_cart()

    @allure.step("Переход на checkout")
    def checkout(self):
        return self.basket_page.checkout()

    @allure.step("Удаление товара")
    def remove_item(self, product_name: str):
        return self.basket_page.remove_item(product_name)

    @allure.step("Проверяем, что товар в корзине")
    def expect_item_in_cart(self, product_name: str):
        return self.basket_page.expect_item_in_cart(product_name)

    @allure.step("Проверяем, что товара нет в корзине")
    def expect_item_not_in_cart(self, product_name: str):
        return self.basket_page.expect_item_not_in_cart(product_name)

    @allure.step("Возвращаем список имен товаров в корзине")
    def get_item_names(self) -> list[str]:
        return self.basket_page.get_item_names()

    @allure.step("Возвращаем список цен товаров в корзине")
    def get_item_price(self) -> list[float]:
        return self.basket_page.get_item_price()

    @allure.step("Возвращаем итоговую цену за товары")
    def get_item_total_price(self) -> float:
        return self.basket_page.get_item_total_price()