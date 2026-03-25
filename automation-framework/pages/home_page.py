from core.base_page import BasePage


class HomePage(BasePage):

    URL = "https://automationexercise.com"

    SIGNUP_LOGIN_BUTTON = "a[href='/login']"
    CONTACT_US_BUTTON = "a[href='/contact_us']"
    TEST_CASES_BUTTON = "a[href='/test_cases']"

    def load(self):
        self.navigate(self.URL)

    def home_visible(self):
        return "automationexercise" in self.page.url
    
    def test_cases_page_visible(self):
        return "test_cases" in self.page.url

    def go_to_signup_login(self):
        self.safe_click(self.SIGNUP_LOGIN_BUTTON)

    def go_to_contact_us(self):
        self.safe_click(self.CONTACT_US_BUTTON)

    def go_to_test_cases(self):
        self.safe_click(self.TEST_CASES_BUTTON)