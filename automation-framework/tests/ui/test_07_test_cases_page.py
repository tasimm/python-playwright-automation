from pages.home_page import HomePage

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Test Cases' button
# 5. Verify user is navigated to test cases page successfully

def test_verify_test_cases_page(page):

    home = HomePage(page)

    # Launch browser and assert visibility
    home.load()
    assert home.home_visible()

    # Click 'Test Cases' button
    home.go_to_test_cases()

    # Verify navigation
    assert home.test_cases_page_visible()