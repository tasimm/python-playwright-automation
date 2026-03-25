import os
from pages.home_page import HomePage
from pages.contact_page import ContactPage

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Contact Us' button
# 5. Verify 'GET IN TOUCH' is visible
# 6. Enter name, email, subject and message
# 7. Upload file
# 8. Click 'Submit' button
# 9. Click OK button
# 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
# 11. Click 'Home' button and verify that landed to home page successfully

def test_contact_form(page):

    home = HomePage(page)
    contact = ContactPage(page)

    # Launch browser and assert visibility
    home.load()
    assert home.home_visible()

    # Click 'Contact Us' button and assert 'GET IN TOUCH' is visible
    home.go_to_contact_us()
    assert contact.verify_get_in_touch_visible()

    # Enter name, email, subject and message
    contact.fill_contact_form(
        "Test User",
        "test@test.com",
        "Test Subject",
        "Test Message"
    )

    # Upload file
    contact.upload_file("test_data/test_file.txt")

    # Click 'Submit' button and Click OK popup
    contact.submit_form_and_accept_alert()

    # Verify success message
    contact.wait_for_success_message()

    # Click 'Home' button and verify that landed to home page successfully
    contact.click_home()
    assert home.home_visible()