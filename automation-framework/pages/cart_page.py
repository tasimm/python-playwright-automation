class CartPage:

    CART_ITEMS = ".cart_description"

    def __init__(self, page):
        self.page = page

    def cart_has_items(self):
        self.page.wait_for_selector(self.CART_ITEMS, timeout=5000)
        return self.page.locator(self.CART_ITEMS).count() > 0