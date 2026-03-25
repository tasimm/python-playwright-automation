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
    SIGNUP_ERROR_MESSAGE = "text=Email Address already exist!"

    def load(self):
        self.navigate(self.LOGIN_URL)

    # ---------- LOGIN ----------

    def wait_for_login_page(self): # Wait function for /login page
        expect(self.page.locator(self.LOGIN_HEADER)).to_be_visible(timeout=5000)

    def login_form_visible(self): # Assert "Login to your account" is visible on /login
        return self.page.locator(self.LOGIN_HEADER).is_visible()

    def login(self, email, password): # Log in function
        self.page.fill(self.LOGIN_EMAIL_INPUT, email)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def wait_for_login_success(self): # Wait function for asserting logged in
        expect(self.page.locator(self.LOGGED_IN_TEXT)).to_be_visible(timeout=7000)

    def logged_in_visible(self): # Assert "Logged in as" is visible on /login
        return self.page.locator(self.LOGGED_IN_TEXT).is_visible()

    def wait_for_login_error(self): # Wait function for log in error
        expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible(timeout=5000)
    
    def error_visible(self): # Assert log in error is visible
        return self.page.locator(self.ERROR_MESSAGE).is_visible()
    
    def logout(self): # Log out function
        self.safe_click(self.LOGOUT_BUTTON)

    # ---------- SIGNUP ENTRY ----------

    def start_signup(self, name, email): # Sign up function on /login page
        self.fill(self.NAME_INPUT, name)
        self.fill(self.SIGNUP_EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)

    def new_user_signup_visible(self): # Assert "New User Signup!" header is visible on /login page
        return self.page.locator(self.NEW_USER_HEADER).is_visible()
    
    def wait_for_signup_error(self): # Wait function for sign up error
        expect(self.page.locator(self.SIGNUP_ERROR_MESSAGE)).to_be_visible(timeout=5000)

    def signup_error_visible(self): # Assert "Email Address already exist!"
        return self.page.locator(self.SIGNUP_ERROR_MESSAGE).is_visible()