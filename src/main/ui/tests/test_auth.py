from playwright.sync_api import expect
from src.main.ui.pages.catalog_page import CatalogPage
from src.main.ui.pages.login_page import LoginPage
from src.main.ui.steps.login_steps import LoginSteps


def test_auth(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("standard_user", "secret_sauce")

    catalog_page = CatalogPage(page)
    assert catalog_page.get_product_count() > 0, "Ожидаем товары на странице каталога"


def test_invalid_auth(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("locked_out_user", "secret_sauce")

    error_text = steps.get_error_text()
    assert "locked out" in error_text, "Ожидаем сообщение о заблокированном пользователе"

def test_logout(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("standard_user", "secret_sauce")

    catalog_page = CatalogPage(page)
    assert catalog_page.get_product_count() > 0, "Ожидаем товары на странице каталога"

    catalog_page.logout()
    expect(page).to_have_url(LoginPage.URL)


def test_logout_for_visual_user(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("visual_user", "secret_sauce")

    catalog_page = CatalogPage(page)
    assert catalog_page.get_product_count() > 0, "Ожидаем товары на странице каталога"

    catalog_page.logout()
    expect(page).to_have_url(LoginPage.URL)
    


