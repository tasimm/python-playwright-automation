from pages.home_page import HomePage
from pages.login_page import LoginPage

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter correct email address and password
# 7. Click 'login' button
# 8. Verify that 'Logged in as username' is visible
# 9. Click 'Logout' button
# 10. Verify that user is navigated to login page

def test_logout(page):

    home = HomePage(page)
    login = LoginPage(page)

    # Launch browser and assert visibility
    home.load()
    assert home.home_visible()

    # Click "Signup/Login" button
    home.go_to_signup_login()

    # Log in with existing test account
    login.login("test123user123@test.com", "password123")
    login.wait_for_login_success()
    assert login.logged_in_visible()

    # Click "Logout"
    login.logout()

    # Verify user is redirected to login page
    login.wait_for_login_page()
    assert login.login_form_visible()