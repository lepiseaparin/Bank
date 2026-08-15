from src.main.ui.pages.catalog_page import CatalogPage
from src.main.ui.steps.catalog_steps import CatalogSteps
from src.main.ui.steps.login_steps import LoginSteps


def test_count_catalog(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    assert steps.get_product_count() == 6


def test_sorted_by_name(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    steps.sort_items("az")
    assert steps.get_product_names() == sorted(steps.get_product_names())


def test_reverse_sorted_by_name(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    steps.sort_items("za")
    assert steps.get_product_names() == sorted(steps.get_product_names(), reverse=True)


def test_sort_by_price(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    steps.sort_items("lohi")
    assert steps.get_product_prices() == sorted(steps.get_product_prices())

    steps.sort_items("hilo")
    assert steps.get_product_prices() == sorted(steps.get_product_prices(), reverse=True)


def test_add_to_cart(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    steps.add_to_cart("Sauce Labs Bike Light")
    assert steps.get_cart_count() == 1


def test_add_and_remove_to_cart(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    steps.add_to_cart("Sauce Labs Onesie")
    assert steps.get_cart_count() == 1

    steps.remove_from_cart("Sauce Labs Onesie")
    assert steps.get_cart_count() == 0


def test_product_details_onesie(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")
    name, price, detail_name, detail_price = steps.open_product_details("Sauce Labs Onesie")

    assert name == detail_name
    assert price == detail_price


def test_product_details_jacket(page):
    catalog = CatalogPage(page)
    catalog.login("standard_user", "secret_sauce")

    name, price, detail_name, detail_price = catalog.open_product_details("Sauce Labs Fleece Jacket")

    assert name == detail_name
    assert price == detail_price


def test_logout(page):
    login = LoginSteps(page)
    catalog = CatalogSteps(page)

    login.open_login_page().login("standard_user", "secret_sauce")
    assert catalog.get_product_count() > 0, "Ожидаем, что в каталоге есть товары"

    catalog.logout()
    assert page.url == "https://www.saucedemo.com/", "Ожидаем возврат на страницу логина"


def test_logout_visual_user(page):
    login = LoginSteps(page)
    catalog = CatalogSteps(page)

    login.open_login_page().login("visual_user", "secret_sauce")
    assert catalog.get_product_count() > 0, "Ожидаем, что в каталоге есть товары"

    catalog.logout()
    assert page.url == login.LOGIN_URL, "Ожидаем возврат на страницу логина"