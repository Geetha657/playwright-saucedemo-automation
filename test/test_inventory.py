from playwright.sync_api import Page

from pages.inventory_page import InventoryPage


def test_sort_products_price_low_to_high(logged_in_page: Page):

    inventory_page = InventoryPage(logged_in_page)

    inventory_page.sort_by_price_low_to_high()

    actual_prices = inventory_page.get_product_prices()

    expected_prices = sorted(actual_prices)

    assert actual_prices == expected_prices


def test_sort_products_price_high_to_low(logged_in_page: Page):

    inventory_page = InventoryPage(logged_in_page)

    inventory_page.sort_by_price_high_to_low()

    actual_prices = inventory_page.get_product_prices()

    expected_prices = sorted(actual_prices, reverse=True)

    assert actual_prices == expected_prices


def test_sort_products_name_a_to_z(logged_in_page: Page):

    inventory_page = InventoryPage(logged_in_page)

    inventory_page.sort_by_name_a_to_z()

    actual_names = inventory_page.get_product_names()

    expected_names = sorted(actual_names)

    assert actual_names == expected_names


def test_sort_products_name_z_to_a(logged_in_page: Page):

    inventory_page = InventoryPage(logged_in_page)

    inventory_page.sort_by_name_z_to_a()

    actual_names = inventory_page.get_product_names()

    expected_names = sorted(actual_names, reverse=True)

    assert actual_names == expected_names