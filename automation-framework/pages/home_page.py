from core.base_page import BasePage

class HomePage(BasePage):

    URL = "https://automationexercise.com"

    def load(self):
        self.navigate(self.URL)

    def is_loaded(self):
        return "Automation Exercise" in self.get_title()