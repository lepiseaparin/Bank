from playwright.sync_api import expect


def test_full(auth_page):


    auth_page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()
    auth_page.locator('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()

    auth_page.locator(".shopping_cart_link").click()

    jacket_name = auth_page.locator('.inventory_item_name', has_text="Sauce Labs Fleece Jacket")
    expect(jacket_name).to_be_visible()
    t_shirt_name = auth_page.locator('.inventory_item_name', has_text="Test.allTheThings() T-Shirt (Red)")
    expect(t_shirt_name).to_be_visible()

    prices_text = auth_page.locator(".inventory_item_price").all_text_contents()
    prices = [float(p.replace("$", "")) for p in prices_text]
    expected_total = sum(prices)

    auth_page.locator("#checkout").click()

    auth_page.fill("#first-name", "Alexei")
    auth_page.fill("#last-name", "Kunershvili")
    auth_page.fill("#postal-code", "113235")
    auth_page.locator("#continue").click()

    item_total_text = auth_page.locator(".summary_subtotal_label").inner_text()
    item_total_value = float(item_total_text.split("$")[1])
    assert item_total_value == expected_total, f"Ожидаемая сумма товаров: {expected_total} не совпадает с действительным: {item_total_value}"

    tax_text = auth_page.locator('.summary_tax_label').inner_text()
    tax_value = float(tax_text.split("$")[1])

    total_text = auth_page.locator('.summary_total_label').inner_text()
    total_value = float(total_text.split("$")[1])

    assert expected_total + tax_value == total_value, f"Ожидаемая сумма товаров: {expected_total + tax_value} не совпадает с действительным {total_value}"

    auth_page.locator('#finish').click()

    expect(auth_page.locator('[data-test="complete-header"]')).to_have_text("Thank you for your order!")

def test_negative_full(auth_page):
    auth_page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()
    auth_page.locator('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()

    auth_page.locator(".shopping_cart_link").click()

    jacket_name = auth_page.locator('.inventory_item_name', has_text="Sauce Labs Fleece Jacket")
    expect(jacket_name).to_be_visible()

    auth_page.locator("#checkout").click()

    auth_page.fill("#first-name", "Alexei")
    auth_page.fill("#last-name", "Kunershvili")
    auth_page.locator("#continue").click()

    error_msg = auth_page.locator('[data-test="error"]')
    expect(error_msg).to_be_visible()
    expect(error_msg).to_have_text("Error: Postal Code is required")






