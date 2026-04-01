from core.base_page import BasePage
from playwright.sync_api import expect

class ProductsPage:

    URL = "https://automationexercise.com/products"

    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    PRODUCT_LIST = ".features_items"
    SEARCH_RESULTS = ".productinfo"
    SEARCHED_PRODUCTS_HEADER = "h2:has-text('Searched Products')"

    ADD_TO_CART_BUTTON = ".product-overlay a.add-to-cart"
    VIEW_CART_BUTTON = "a[href='/view_cart']"

    # Product listing / navigation
    ALL_PRODUCTS_HEADER = "h2:has-text('All Products')"
    FIRST_VIEW_PRODUCT = ".product-image-wrapper a:has-text('View Product')"

    # Product detail page elements
    PRODUCT_NAME = ".product-information h2"
    CATEGORY = ".product-information p"
    PRICE = ".product-information span span"
    AVAILABILITY = "text=Availability:"
    CONDITION = "text=Condition:"
    BRAND = "text=Brand:"

    def __init__(self, page):
        # Initialize page instance for Playwright interactions
        self.page = page

    def load(self):
        # Navigate directly to the products page
        self.page.goto(self.URL)

    # ---------- SEARCH ----------

    def search_product(self, product_name):
        # Enter product name and trigger search
        self.page.fill(self.SEARCH_INPUT, product_name)
        self.page.click(self.SEARCH_BUTTON)

    def products_visible(self):
        # Check if the main product list is displayed
        return self.page.locator(self.PRODUCT_LIST).is_visible()
    
    def search_results_visible(self):
        # Verify at least one search result is visible
        return self.page.locator(self.SEARCH_RESULTS).first.is_visible()
    
    # ---------- CART ----------

    def add_first_product_to_cart(self):
        # Hover first product and add it to the cart
        self.page.hover(".product-image-wrapper")
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()
        # Wait for modal
        self.page.wait_for_selector("#cartModal", timeout=5000)

    def view_cart(self):
        # Open cart from modal and wait for navigation
        self.page.locator("#cartModal a[href='/view_cart']").click()
        self.page.wait_for_url("**/view_cart")

    # ---------- PRODUCT LIST / NAVIGATION ----------

    def verify_all_products_page(self):
        # Ensure user is on the All Products page
        expect(self.page.locator(self.ALL_PRODUCTS_HEADER)).to_be_visible(timeout=5000)

    def click_first_view_product(self):
        # Open the first product's detail page
        self.page.locator(self.FIRST_VIEW_PRODUCT).first.click()

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