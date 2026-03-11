from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, text):
        self.page.fill(selector, text)

    def is_visible(self, selector):
        return self.page.locator(selector).is_visible()

    def get_title(self):
        return self.page.title()