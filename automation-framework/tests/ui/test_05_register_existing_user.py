from pages.home_page import HomePage
from pages.login_page import LoginPage

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'New User Signup!' is visible
# 6. Enter name and already registered email address
# 7. Click 'Signup' button
# 8. Verify error 'Email Address already exist!' is visible

def test_register_existing_user(page):

    home = HomePage(page)
    login = LoginPage(page)

    # Launch browser and assert visibility
    home.load()
    assert home.home_visible()

    # Click "Signup/Login" button and assert "New User Signup!" is visible
    home.go_to_signup_login()
    assert login.new_user_signup_visible()

    # Enter existing user email into signup
    login.start_signup("Test User", "test123user123@test.com")

    # Assert error
    login.wait_for_signup_error()
    assert login.signup_error_visible()