from pages.home_page import HomePage

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Scroll down to footer
# 5. Verify text 'SUBSCRIPTION'
# 6. Enter email address in input and click arrow button
# 7. Verify success message 'You have been successfully subscribed!' is visible
def test_verify_subscription_home_page(page):

    home = HomePage(page)

    # Launch browser and assert visibility
    home.load()
    assert home.home_visible()

    # Scroll down to footer
    home.scroll_to_footer()

    # Verify text 'SUBSCRIPTION'
    home.verify_subscription_visible()

    # Enter email address in input and click arrow button
    home.subscribe("test123user123@test.com")

    # Verify success message 'You have been successfully subscribed!' is visible
    home.wait_for_subscription_success()
    assert home.subscription_success_visible()