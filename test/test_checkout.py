
import pytest

from playwright.sync_api import Page, expect


from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_successful_checkout(logged_in_page: Page):

    

    # Step 2: Add product
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart("Sauce Labs Backpack")

    # Step 3: Open cart
    cart_page = CartPage(logged_in_page)
    cart_page.open_cart()

    # Step 4: Click checkout
    cart_page.checkout()

    # Step 5: Enter customer details
    checkout_page = CheckoutPage(logged_in_page)

    checkout_page.enter_customer_details(
        "Geetha",
        "Vasa",
        "500001"
    )

    # Step 6: Continue
    checkout_page.continue_checkout()

    # Step 7: Finish
    checkout_page.finish_checkout()

    # Step 8: Verify success
    expect(checkout_page.complete_message).to_have_text(
        "Thank you for your order!"
    )
    

@pytest.mark.parametrize("first,last,postal,error", [
    ("", "Vasa", "500001", "First Name is required"),
    ("Geetha", "", "500001", "Last Name is required"),
    ("Geetha", "Vasa", "", "Postal Code is required"),
    ])
def test_checkout_missing_information(logged_in_page: Page, first, last, postal, error):

    

    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart("Sauce Labs Backpack")

    cart_page = CartPage(logged_in_page)
    cart_page.open_cart()
    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_page)

    checkout_page.enter_customer_details(first, last, postal)

    checkout_page.continue_checkout()

    expect(checkout_page.error_message).to_contain_text(error)