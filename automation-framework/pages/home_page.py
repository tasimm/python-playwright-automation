from core.base_page import BasePage


class HomePage(BasePage):

    URL = "https://automationexercise.com"

    SIGNUP_LOGIN_BUTTON = "a[href='/login']"

    def load(self):
        self.navigate(self.URL)

    def home_visible(self):
        return "automationexercise" in self.page.url

    def go_to_signup_login(self):
        self.click(self.SIGNUP_LOGIN_BUTTON)