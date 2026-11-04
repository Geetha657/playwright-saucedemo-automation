from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_one_product_to_cart(logged_in_page: Page):

    inventory_page = InventoryPage(logged_in_page)

    inventory_page.add_to_cart("Sauce Labs Backpack")

    expect(inventory_page.cart_badge).to_have_text("1")


def test_add_two_products_and_remove_one(logged_in_page: Page):

    inventory_page = InventoryPage(logged_in_page)

    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bike Light")

    expect(inventory_page.cart_badge).to_have_text("2")

    inventory_page.remove_from_cart("Sauce Labs Backpack")

    expect(inventory_page.cart_badge).to_have_text("1")


def test_cart_contains_correct_products(logged_in_page: Page):

    inventory_page = InventoryPage(logged_in_page)

    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bike Light")

    cart_page = CartPage(logged_in_page)

    cart_page.open_cart()

    expect(cart_page.cart_items).to_have_count(2)

    expect(cart_page.product_names).to_contain_text([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ])