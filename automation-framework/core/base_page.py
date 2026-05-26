from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, selector):
        self.page.click(selector)

    def hover(self, selector):
        # Hover over an element
        self.page.locator(selector).hover()

    def fill(self, selector, text):
        self.page.fill(selector, text)

    def is_visible(self, selector):
        return self.page.locator(selector).is_visible()

    def get_title(self):
        return self.page.title()
    
    def handle_ads(self):
        try:
            # Try to close common ad overlays (iframe or button)
            self.page.locator("iframe").first.wait_for(timeout=2000)

            # Remove ALL iframes (safe for this site)
            self.page.evaluate("""
            document.querySelectorAll('iframe').forEach(el => el.remove());
            """)

            # Also remove possible overlay divs
            self.page.evaluate("""
                document.querySelectorAll('[id*="google"], [class*="overlay"]').forEach(el => el.remove());
            """)

        except:
            pass

    def safe_click(self, selector):
        self.handle_ads()
        self.page.click(selector)