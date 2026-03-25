from core.base_page import BasePage
from playwright.sync_api import expect

class ContactPage(BasePage):

    CONTACT_URL = "https://automationexercise.com/contact_us"

    # Selectors
    GET_IN_TOUCH_HEADER = "h2:has-text('Get In Touch')"
    NAME_INPUT = "input[data-qa='name']"
    EMAIL_INPUT = "input[data-qa='email']"
    SUBJECT_INPUT = "input[data-qa='subject']"
    MESSAGE_INPUT = "textarea[data-qa='message']"
    FILE_UPLOAD = "input[name='upload_file']"
    SUBMIT_BUTTON = "input[data-qa='submit-button']"
    SUCCESS_MESSAGE = ".status.alert.alert-success"
    HOME_BUTTON = "a:has-text('Home')"

# ---------- ACTIONS ----------

    def verify_get_in_touch_visible(self):
        return self.page.locator(self.GET_IN_TOUCH_HEADER).is_visible()
    
    def fill_contact_form(self, name, email, subject, message):
        self.fill(self.NAME_INPUT, name)
        self.fill(self.EMAIL_INPUT, email)
        self.fill(self.SUBJECT_INPUT, subject)
        self.fill(self.MESSAGE_INPUT, message)

    def upload_file(self, file_path):
        self.page.set_input_files(self.FILE_UPLOAD, file_path)

    def submit_form_and_accept_alert(self):
        # Attach handler BEFORE click (like Selenium flow)
        self.page.on("dialog", lambda dialog: dialog.accept())

        self.safe_click(self.SUBMIT_BUTTON)

# ---------- WAITS / ASSERTS ----------

    def wait_for_success_message(self):
        expect(self.page.locator(self.SUCCESS_MESSAGE)).to_be_visible(timeout=5000)

    def success_message_visible(self):
        return self.page.locator(self.SUCCESS_MESSAGE).is_visible()
    
    def click_home(self):
        self.click(self.HOME_BUTTON)