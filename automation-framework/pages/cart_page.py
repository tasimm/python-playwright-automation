from playwright.sync_api import expect
from core.base_page import BasePage

class CartPage(BasePage):

    CART_ITEMS = ".cart_description"
    PRODUCT_PRICE = ".cart_price"
    PRODUCT_QUANTITY = ".cart_quantity"
    PRODUCT_TOTAL = ".cart_total"
    CART_QUANTITY = ".cart_quantity button"
    REMOVE_PRODUCT_BUTTON = ".cart_quantity_delete"

    def cart_has_items(self):
        self.page.wait_for_selector(self.CART_ITEMS, timeout=5000)
        return self.page.locator(self.CART_ITEMS).count() > 0
    
    def verify_products_in_cart(self):
        # Ensure at least two products are in cart
        expect(self.page.locator(self.CART_ITEMS)).to_have_count(2, timeout=5000)

    def get_product_count(self):
        # Return number of products in cart
        return self.page.locator(self.CART_ITEMS).count()
    
    def prices_visible(self):
        # Verify price column is visible
        return self.page.locator(self.PRODUCT_PRICE).first.is_visible()
    
    def quantity_visible(self):
        # Verify quantity column is visible
        return self.page.locator(self.PRODUCT_QUANTITY).first.is_visible()
    
    def total_visible(self):
        # Verify total column is visible
        return self.page.locator(self.PRODUCT_TOTAL).first.is_visible()
    
    def verify_product_quantity(self, quantity):
        # Verify cart quantity matches expected value
        actual_quantity = self.page.locator(self.CART_QUANTITY).first.inner_text()
        return actual_quantity == str(quantity)
    
    def remove_first_product(self):
        # Remove the first product from the cart
        self.page.locator(self.REMOVE_PRODUCT_BUTTON).first.click()

        # Wait for row removal
        self.page.wait_for_timeout(1000)

    def cart_empty(self):
        # Verify cart no longer contains products
        return self.page.locator(self.CART_ITEMS).count() == 0