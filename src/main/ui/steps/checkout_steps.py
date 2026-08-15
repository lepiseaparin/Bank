import allure
from src.main.ui.pages.checkout_page import CheckoutPage
from playwright.sync_api import Page


class CheckoutSteps:
    def __init__(self, page):
        self.page = page
        self.checkout = CheckoutPage(page)


    @allure.step("Заполняем поля checkout: {first_name}, {last_name}, {postal_code}")
    def start_checkout(self, first_name: str, last_name: str, postal_code: str):
        return self.checkout.start_checkout(first_name=first_name, last_name=last_name, postal_code=postal_code)

    @allure.step("Завершаем checkout")
    def finish_checkout(self):
        return self.checkout.finish_checkout()

    @allure.step("Получаем текст ошибки")
    def get_error_text(self):
        return self.checkout.get_error_text()

    @allure.step("Получаем сообщение о выполнении")
    def get_success_text(self):
        return self.checkout.get_success_text()

    @allure.step("Получаем итоговую цену товаров")
    def get_item_total(self) -> float:
        return self.checkout.get_item_total()

    @allure.step("Получаем итоговую цену после continue")
    def get_item_total_after_continue(self) -> float:
        return self.checkout.get_item_total_after_continue()