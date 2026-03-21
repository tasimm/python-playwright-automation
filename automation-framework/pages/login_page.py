from core.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):

    LOGIN_URL = "https://automationexercise.com/login"

    # Log in selectors
    LOGIN_EMAIL_INPUT = 'input[data-qa="login-email"]'
    PASSWORD_INPUT = 'input[data-qa="login-password"]'
    LOGIN_BUTTON = 'button[data-qa="login-button"]'
    ERROR_MESSAGE = "form[action='/login'] p"

    # Sign up selectors
    NAME_INPUT = 'input[data-qa="signup-name"]'
    SIGNUP_EMAIL_INPUT = 'input[data-qa="signup-email"]'
    SIGNUP_BUTTON = 'button[data-qa="signup-button"]'

    # Signup/Login page headers
    LOGIN_HEADER = "h2:has-text('Login to your account')"
    NEW_USER_HEADER = "h2:has-text('New User Signup!')"
    LOGGED_IN_TEXT = "a:has-text('Logged in as')"
    LOGOUT_BUTTON = "a[href='/logout']"

    def load(self):
        self.navigate(self.LOGIN_URL)

    # ---------- LOGIN ----------

    def login_form_visible(self):
        return self.page.locator(self.LOGIN_HEADER).is_visible()

    def login(self, email, password):
        self.page.fill(self.LOGIN_EMAIL_INPUT, email)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def wait_for_login_success(self):
        expect(self.page.locator(self.LOGGED_IN_TEXT)).to_be_visible(timeout=7000)

    def wait_for_login_error(self):
        expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible(timeout=5000)

    def logged_in_visible(self):
        return self.page.locator(self.LOGGED_IN_TEXT).is_visible()
    
    def error_visible(self):
        return self.page.locator(self.ERROR_MESSAGE).to_be_visible()
    
    def logout(self):
        self.click(self.LOGOUT_BUTTON)

    # ---------- SIGNUP ENTRY ----------

    def start_signup(self, name, email):
        self.fill(self.NAME_INPUT, name)
        self.fill(self.SIGNUP_EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)

    # ---------- STATE CHECKS ----------

    def login_form_visible(self):
        return self.page.locator(self.LOGIN_HEADER).is_visible()
    
    def new_user_signup_visible(self):
        return self.page.locator(self.NEW_USER_HEADER).is_visible()