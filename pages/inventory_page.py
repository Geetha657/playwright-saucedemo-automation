from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_to_cart(self, product_name):
        product = self.page.locator(".inventory_item").filter(
            has_text=product_name
        )
        product.get_by_role("button", name="Add to cart").click()

    def remove_from_cart(self, product_name):
        product = self.page.locator(".inventory_item").filter(
            has_text=product_name
        )
        product.get_by_role("button", name="Remove").click()

    def sort_by_price_low_to_high(self):
        self.page.locator(".product_sort_container").select_option("lohi")

    def get_product_prices(self):
        prices = self.page.locator(
            ".inventory_item_price"
        ).all_text_contents()

        return [float(price.replace("$", "")) for price in prices]

    def sort_by_price_high_to_low(self):
        self.page.locator(".product_sort_container").select_option("hilo")

    def sort_by_name_a_to_z(self):
        self.page.locator(".product_sort_container").select_option("az")

    def sort_by_name_z_to_a(self):
        self.page.locator(".product_sort_container").select_option("za")

    def get_product_names(self):
        return self.page.locator(".inventory_item_name").all_text_contents()