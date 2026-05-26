from core.base_page import BasePage
from playwright.sync_api import expect

class ProductsPage(BasePage):

    URL = "https://automationexercise.com/products"

    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    PRODUCT_LIST = ".features_items"
    SEARCH_RESULTS = ".productinfo"
    SEARCHED_PRODUCTS_HEADER = "h2:has-text('Searched Products')"

    # Product listing / navigation
    ALL_PRODUCTS_HEADER = "h2:has-text('All Products')"
    FIRST_VIEW_PRODUCT = ".product-image-wrapper a:has-text('View Product')"
    PRODUCT_CARDS = ".product-image-wrapper"
    ADD_TO_CART_BUTTON = ".product-overlay a.add-to-cart"
    VIEW_CART_BUTTON = "#cartModal a[href='/view_cart']"
    CONTINUE_SHOPPING_BUTTON = "button:has-text('Continue Shopping')"

    # Product detail page elements
    PRODUCT_NAME = ".product-information h2"
    CATEGORY = ".product-information p"
    PRICE = ".product-information span span"
    AVAILABILITY = "text=Availability:"
    CONDITION = "text=Condition:"
    BRAND = "text=Brand:"
    QUANTITY_INPUT = "#quantity"
    ADD_TO_CART_DETAIL_BUTTON = "button.cart"

    def load(self):
        # Navigate directly to the products page
        self.navigate(self.URL)

    # ---------- SEARCH ----------

    def search_product(self, product_name):
        # Enter product name and trigger search
        self.fill(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def products_visible(self):
        # Check if the main product list is displayed
        return self.page.locator(self.PRODUCT_LIST).is_visible()
    
    def search_results_visible(self):
        # Verify at least one search result is visible
        return self.page.locator(self.SEARCH_RESULTS).first.is_visible()
    
    # ---------- CART ----------

    def view_cart(self):
        # Open cart from modal and wait for navigation
        self.safe_click(self.VIEW_CART_BUTTON)
        self.page.wait_for_url("**/view_cart")

    def set_quantity(self, quantity):
        # Replace default quantity with desired amount
        self.page.locator(self.QUANTITY_INPUT).clear()
        self.fill(self.QUANTITY_INPUT, str(quantity))

    # ---------- PRODUCT LIST / NAVIGATION ----------

    def verify_all_products_page(self):
        # Ensure user is on the All Products page
        expect(self.page.locator(self.ALL_PRODUCTS_HEADER)).to_be_visible(timeout=5000)

    def click_first_view_product(self):
        # Open the first product's detail page
        self.page.locator(self.FIRST_VIEW_PRODUCT).first.click()

    def continue_shopping(self):
        # Click Continue Shopping in modal
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def add_first_product(self):
        # Hover first product and add it to cart
        self.page.locator(self.PRODUCT_CARDS).first.hover()

        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()

        # Wait for cart modal
        self.page.wait_for_selector("#cartModal", timeout=5000)

    def add_second_product(self):
        # Hover and add second product to cart
        self.page.locator(self.PRODUCT_CARDS).nth(1).hover()
        self.page.locator(self.ADD_TO_CART_BUTTON).nth(1).click()
        self.page.wait_for_selector("#cartModal", timeout=5000)

    # ---------- PRODUCT DETAILS ----------

    def verify_product_detail_page(self):
        # Wait for product detail page to load
        expect(self.page.locator(self.PRODUCT_NAME)).to_be_visible(timeout=5000)

    def product_details_visible(self):
        # Verify all key product details are displayed
        return (
            self.page.locator(self.PRODUCT_NAME).is_visible()
            and self.page.locator(self.CATEGORY).first.is_visible()
            and self.page.locator(self.PRICE).is_visible()
            and self.page.locator(self.AVAILABILITY).is_visible()
            and self.page.locator(self.CONDITION).is_visible()
            and self.page.locator(self.BRAND).is_visible()
        )
    
    def verify_searched_products_visible(self):
        # Ensure the searched products header is displayed
        expect(self.page.locator(self.SEARCHED_PRODUCTS_HEADER)).to_be_visible(timeout=5000)

    def add_product_from_detail_page(self):
        # Add product to cart from detail page
        self.click(self.ADD_TO_CART_DETAIL_BUTTON)

        # Wait for cart modal to appear
        self.page.wait_for_selector("#cartModal", timeout=5000)

    def product_detail_visible(self):
        # Verify product detail page is displayed
        return self.page.locator(self.PRODUCT_NAME).is_visible()