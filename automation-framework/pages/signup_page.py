from core.base_page import BasePage
from playwright.sync_api import expect

# Sign up page selectors
class SignupPage(BasePage):

    LOGIN_URL = "https://automationexercise.com/login"

    ACCOUNT_INFO_HEADER = 'b:has-text("Enter Account Information")'

    TITLE_MR = '#id_gender1'
    PASSWORD_INPUT = '#password'

    DAY_SELECT = '#days'
    MONTH_SELECT = '#months'
    YEAR_SELECT = '#years'

    NEWSLETTER_CHECKBOX = "#newsletter"
    OFFERS_CHECKBOX = "#optin"

    FIRST_NAME = '#first_name'
    LAST_NAME = '#last_name'
    COMPANY = "#company"
    ADDRESS = '#address1'
    ADDRESS2 = "#address2"
    COUNTRY = '#country'
    STATE = '#state'
    CITY = '#city'
    ZIPCODE = '#zipcode'
    MOBILE = '#mobile_number'

    CREATE_ACCOUNT_BUTTON = 'button[data-qa="create-account"]'
    ACCOUNT_CREATED_HEADER = 'b:has-text("Account Created!")'

    CONTINUE_BUTTON = "a[data-qa='continue-button']"
    ACCOUNT_DELETED_HEADER = "b:has-text('Account Deleted!')"
    DELETE_ACCOUNT_BUTTON = "a[href='/delete_account']"

    def load(self):
        self.navigate(self.LOGIN_URL)

    def account_form_visible(self):
        self.page.locator(self.ACCOUNT_INFO_HEADER).wait_for()
        return True
    
    # Inserts account data
    def complete_account_creation(self, user_data):
        # Selects "Mr." title
        self.click(self.TITLE_MR)
        # Password
        self.fill(self.PASSWORD_INPUT, user_data["password"])
        # Date of Birth
        self.page.select_option(self.DAY_SELECT, user_data["day"])
        self.page.select_option(self.MONTH_SELECT, user_data["month"])
        self.page.select_option(self.YEAR_SELECT, user_data["year"])
        # Checkboxes
        self.click(self.NEWSLETTER_CHECKBOX)
        self.click(self.OFFERS_CHECKBOX)

        self.fill(self.FIRST_NAME, user_data["first_name"])
        self.fill(self.LAST_NAME, user_data["last_name"])
        self.fill(self.COMPANY, "Test Company")

        self.fill(self.ADDRESS, user_data["address"])
        self.fill(self.ADDRESS2, "Suite 1")

        self.page.select_option(self.COUNTRY, user_data["country"])

        self.fill(self.STATE, user_data["state"])
        self.fill(self.CITY, user_data["city"])
        self.fill(self.ZIPCODE, user_data["zipcode"])

        self.fill(self.MOBILE, user_data["mobile_number"])
        # Selects "Create Account" button
        self.click(self.CREATE_ACCOUNT_BUTTON)

    # Asserts that the "Account Created!" header is seen after sucessfully creating account
    def account_created(self):
        self.page.locator(self.ACCOUNT_CREATED_HEADER).wait_for()
        return True
    
    def click_continue(self):
        self.safe_click(self.CONTINUE_BUTTON)

    def delete_account(self):
        button = self.page.locator(self.DELETE_ACCOUNT_BUTTON)

        # Wait for it to exist AND be visible
        expect(button).to_be_visible(timeout=7000)

        # Ensure it's actually interactable
        button.scroll_into_view_if_needed()

        # Extra safety: wait for page stability
        self.page.wait_for_load_state("domcontentloaded")

        button.click()

    def account_deleted(self):
        self.page.locator(self.ACCOUNT_DELETED_HEADER).wait_for()
        return True