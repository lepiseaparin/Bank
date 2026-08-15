import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="function")
def auth_page(page):
    page.goto("https://www.saucedemo.com")
    # аутентификация на сайте
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.locator("#login-button").click()

    return page



