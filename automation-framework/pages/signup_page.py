from core.base_page import BasePage

# Sign up page selectors
class SignupPage(BasePage):

    LOGIN_URL = "https://automationexercise.com/login"

    NAME_INPUT = 'input[data-qa="signup-name"]'
    EMAIL_INPUT = 'input[data-qa="signup-email"]'
    SIGNUP_BUTTON = 'button[data-qa="signup-button"]'

    ACCOUNT_INFO_HEADER = 'b:has-text("Enter Account Information")'

    TITLE_MR = '#id_gender1'
    PASSWORD_INPUT = '#password'

    DAY_SELECT = '#days'
    MONTH_SELECT = '#months'
    YEAR_SELECT = '#years'

    FIRST_NAME = '#first_name'
    LAST_NAME = '#last_name'
    ADDRESS = '#address1'
    COUNTRY = '#country'
    STATE = '#state'
    CITY = '#city'
    ZIPCODE = '#zipcode'
    MOBILE = '#mobile_number'

    CREATE_ACCOUNT_BUTTON = 'button[data-qa="create-account"]'

    ACCOUNT_CREATED_HEADER = 'b:has-text("Account Created!")'

    def load(self):
        self.navigate(self.LOGIN_URL)

    # Sign up info on login page
    def start_signup(self, name, email):
        self.fill(self.NAME_INPUT, name)
        self.fill(self.EMAIL_INPUT, email)
        self.click(self.SIGNUP_BUTTON)

    def account_form_visible(self):
        self.page.locator(self.ACCOUNT_INFO_HEADER).wait_for()
        return True
    
    # Inserts necessary account data
    def complete_account_creation(self, user_data):

        self.click(self.TITLE_MR)

        self.fill(self.PASSWORD_INPUT, user_data["password"])

        self.page.select_option(self.DAY_SELECT, "10")
        self.page.select_option(self.MONTH_SELECT, "5")
        self.page.select_option(self.YEAR_SELECT, "1995")

        self.fill(self.FIRST_NAME, user_data["name"].split()[0])
        self.fill(self.LAST_NAME, "Test")

        self.fill(self.ADDRESS, "123 Test Street")

        self.page.select_option(self.COUNTRY, "United States")

        self.fill(self.STATE, "Ohio")
        self.fill(self.CITY, "Akron")
        self.fill(self.ZIPCODE, "44301")

        self.fill(self.MOBILE, "3305551234")

        self.click(self.CREATE_ACCOUNT_BUTTON)

    # Asserts that the "Account Created!" header is seen after sucessfully creating account
    def account_created(self):

        self.page.locator(self.ACCOUNT_CREATED_HEADER).wait_for()

        return True