class ProductsPage:

    URL = "https://automationexercise.com/products"

    SEARCH_INPUT = "#search_product"
    SEARCH_BUTTON = "#submit_search"
    PRODUCT_LIST = ".features_items"
    SEARCH_RESULTS = ".productinfo"

    ADD_TO_CART_BUTTON = ".product-overlay a.add-to-cart"
    VIEW_CART_BUTTON = "a[href='/view_cart']"

    def __init__(self, page):
        self.page = page

    def load(self):
        self.page.goto(self.URL)

    def search_product(self, product_name):
        self.page.fill(self.SEARCH_INPUT, product_name)
        self.page.click(self.SEARCH_BUTTON)

    def products_visible(self):
        return self.page.locator(self.PRODUCT_LIST).is_visible()
    
    def search_results_visible(self):
        return self.page.locator(self.SEARCH_RESULTS).first.is_visible()
    
    def add_first_product_to_cart(self):
        self.page.hover(".product-image-wrapper")
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()
        # Wait for modal
        self.page.wait_for_selector("#cartModal", timeout=5000)

    def view_cart(self):
        # Click "View Cart" inside the modal
        self.page.locator("#cartModal a[href='/view_cart']").click()
        # Wait for navigation
        self.page.wait_for_url("**/view_cart")