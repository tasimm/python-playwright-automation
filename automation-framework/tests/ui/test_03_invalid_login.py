from pages.home_page import HomePage
from pages.login_page import LoginPage

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter incorrect email address and password
# 7. Click 'login' button
# 8. Verify error 'Your email or password is incorrect!' is visible

def test_login_with_invalid_credentials(page):

    home = HomePage(page)
    login = LoginPage(page)

    # Launch browser and assert visibility
    home.load()
    assert home.home_visible()

    # Click "Signup/Login" button and assert visibility
    home.go_to_signup_login()
    assert login.login_form_visible()

    # Enter incorrect credentials
    login.login("fakeuser123@test.com", "wrongpassword")

    # Wait for and assert error
    login.wait_for_login_error()
    assert login.error_visible()