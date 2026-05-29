from core.base_page import BasePage
from playwright.sync_api import expect

class CheckoutPage(BasePage):

    # Cart / checkout
    PROCEED_TO_CHECKOUT_BUTTON = "a:has-text('Proceed To Checkout')"
    REGISTER_LOGIN_BUTTON = "u:has-text('Register / Login')"

    # Checkout page
    ADDRESS_DETAILS_HEADER = "h2:has-text('Address Details')"
    REVIEW_ORDER_HEADER = "h2:has-text('Review Your Order')"

    COMMENT_BOX = "textarea[name='message']"
    PLACE_ORDER_BUTTON = "a:has-text('Place Order')"

    # Payment form
    NAME_ON_CARD = "input[data-qa='name-on-card']"
    CARD_NUMBER = "input[data-qa='card-number']"
    CVC = "input[data-qa='cvc']"
    EXPIRY_MONTH = "input[data-qa='expiry-month']"
    EXPIRY_YEAR = "input[data-qa='expiry-year']"

    PAY_CONFIRM_BUTTON = "button[data-qa='pay-button']"

    # Success
    ORDER_SUCCESS = "text=Congratulations! Your order has been confirmed!"

    # ---------- CHECKOUT ----------

    def proceed_to_checkout(self):
        # Proceed to checkout from cart page
        self.safe_click(self.PROCEED_TO_CHECKOUT_BUTTON)

    def click_register_login(self):
        # Open login/signup page from checkout modal
        self.safe_click(self.REGISTER_LOGIN_BUTTON)

    # ---------- VALIDATION ----------

    def checkout_page_visible(self):
        # Verify checkout sections are visible
        return (
            self.page.locator(self.ADDRESS_DETAILS_HEADER).is_visible()
            and self.page.locator(self.REVIEW_ORDER_HEADER).is_visible()
        )
    
    # ---------- ORDER ----------

    def enter_order_comment(self, comment):
        # Enter comment before placing order
        self.fill(self.COMMENT_BOX, comment)

    def place_order(self):
        # Submit order placement
        self.safe_click(self.PLACE_ORDER_BUTTON)

    # ---------- PAYMENT ----------

    def fill_payment_details(self):
        # Fill payment form details
        self.fill(self.NAME_ON_CARD, "Test User")
        self.fill(self.CARD_NUMBER, "4111111111111111")
        self.fill(self.CVC, "123")
        self.fill(self.EXPIRY_MONTH, "12")
        self.fill(self.EXPIRY_YEAR, "2030")

    def pay_and_confirm_order(self):
        # Confirm payment submission
        self.click(self.PAY_CONFIRM_BUTTON)

    # ---------- SUCCESS ----------

    def wait_for_order_success(self):
        # Wait for successful order message
        expect(self.page.locator(self.ORDER_SUCCESS)).to_be_visible(timeout=10000)

    def order_success_visible(self):
        # Verify successful order message is visible
        return self.page.locator(self.ORDER_SUCCESS).is_visible()