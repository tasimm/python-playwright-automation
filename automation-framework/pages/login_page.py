from core.base_page import BasePage
from playwright.sync_api import expect


class LoginPage(BasePage):

    LOGIN_URL = "https://automationexercise.com/login"

    EMAIL_INPUT = 'input[data-qa="login-email"]'
    PASSWORD_INPUT = 'input[data-qa="login-password"]'
    LOGIN_BUTTON = 'button[data-qa="login-button"]'
    ERROR_MESSAGE = "form[action='/login'] p"

    def load(self):
        self.navigate(self.LOGIN_URL)

    def login(self, email, password):
        self.page.fill(self.EMAIL_INPUT, email)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

        # Wait for either success or error state
        self.page.wait_for_load_state("networkidle")

    def error_visible(self):
        error = self.page.locator(self.ERROR_MESSAGE)

        try:
            expect(error).to_be_visible(timeout=5000)
            return True
        except:
            return False