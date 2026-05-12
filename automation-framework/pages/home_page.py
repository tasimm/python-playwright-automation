from playwright.sync_api import expect
from core.base_page import BasePage


class HomePage(BasePage):

    URL = "https://automationexercise.com"

    # Home Page buttons
    SIGNUP_LOGIN_BUTTON = "a[href='/login']"
    CONTACT_US_BUTTON = "a[href='/contact_us']"
    TEST_CASES_BUTTON = "a[href='/test_cases']"
    PRODUCTS_BUTTON = "a[href='/products']"
    CART_BUTTON = "a[href='/view_cart']"
    
    SUBSCRIPTION_HEADER = "h2:has-text('Subscription')"
    SUBSCRIPTION_EMAIL_INPUT = "#susbscribe_email"
    SUBSCRIPTION_BUTTON = "#subscribe"
    SUBSCRIPTION_SUCCESS = "text=You have been successfully subscribed!"

    
    def load(self):
        # Load browser and navigate to base URL
        self.navigate(self.URL)

    def scroll_to_footer(self):
        # Scroll to bottom of page
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def home_visible(self):
        # Verify home page is visible
        return "automationexercise" in self.page.url
    
    def test_cases_page_visible(self):
        # Verify Test Cases page is visible
        return "test_cases" in self.page.url

    # ---------- NAVIGATE ----------
    def go_to_signup_login(self):
        # Navigate to Signup/Login page
        self.safe_click(self.SIGNUP_LOGIN_BUTTON)

    def go_to_contact_us(self):
        # Navigate to Contact Us page
        self.safe_click(self.CONTACT_US_BUTTON)

    def go_to_test_cases(self):
        # Navigate to Test Cases page
        self.safe_click(self.TEST_CASES_BUTTON)

    def go_to_products(self):
        # Navigate to Products page
        self.click(self.PRODUCTS_BUTTON)

    def go_to_cart(self):
        # Navigate to Cart page
        self.click(self.CART_BUTTON)

    # ---------- SUBSCRIBE FUNCTION ----------
    def verify_subscription_visible(self):
        # Verify subscription section is visible
        expect(self.page.locator(self.SUBSCRIPTION_HEADER)).to_be_visible(timeout=5000)

    def subscribe(self, email):
        # Enter email and submit subscription
        self.page.fill(self.SUBSCRIPTION_EMAIL_INPUT, email)
        self.page.click(self.SUBSCRIPTION_BUTTON)

    def wait_for_subscription_success(self):
        # Wait for success message after subscribing
        expect(self.page.locator(self.SUBSCRIPTION_SUCCESS)).to_be_visible(timeout=5000)

    def subscription_success_visible(self):
        # Check if success message is visible
        return self.page.locator(self.SUBSCRIPTION_SUCCESS).is_visible()