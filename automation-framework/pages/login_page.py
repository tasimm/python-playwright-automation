from core.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_URL = "https://automationexercise.com/login"

    EMAIL_INPUT = 'input[data-qa="login-email"]'
    PASSWORD_INPUT = 'input[data-qa="login-password"]'
    LOGIN_BUTTON = 'button[data-qa="login-button"]'
    ERROR_MESSAGE = 'p:has-text("Your email or password is incorrect!")'

    def load(self):
        self.navigate(self.LOGIN_URL)

    def login(self, email, password):
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def error_visible(self):
        self.page.wait_for_selector(self.ERROR_MESSAGE, timeout=5000)
        return self.page.locator(self.ERROR_MESSAGE).is_visible()