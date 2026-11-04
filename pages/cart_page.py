from playwright.sync_api import Page

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.product_names = page.locator(".inventory_item_name")

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()
    def checkout(self):
        self.page.get_by_role("button", name="Checkout").click()    