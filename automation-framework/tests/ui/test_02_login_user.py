from utils.user_factory import generate_user
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from playwright.sync_api import expect

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'Login to your account' is visible
# 6. Enter correct email address and password
# 7. Click 'login' button
# 8. Verify that 'Logged in as username' is visible
# 9. Click 'Delete Account' button
# 10. Verify that 'ACCOUNT DELETED!' is visible

def test_login_user(page):

    user = generate_user()

    home = HomePage(page)
    login = LoginPage(page)
    signup = SignupPage(page)

    # Launch browser, navigate to URL, assert home page is visible
    home.load()
    assert home.home_visible()

    # Click Signup/Login button
    home.go_to_signup_login()

    # Verify "New User Signup" header is visible
    assert login.new_user_signup_visible()

    # Enter name/email + click signup
    login.start_signup(user["name"], user["email"])
    assert signup.account_form_visible()

    # Fill form + submit
    signup.complete_account_creation(user)
    assert signup.account_created()

    # Click continue
    signup.click_continue()

    # Log user out
    login.logout()

    # Verify login form is visible again
    assert login.login_form_visible()

    # Enter user's credentials + login
    login.login(user["email"], user["password"])
    login.wait_for_login_success()
    assert login.logged_in_visible()

    # Wait for navbar to stabilize
    expect(page.locator("a[href='/delete_account']")).to_be_visible(timeout=7000)

    # Ad typically appears at this point - we move past it
    signup.handle_ads()

    # Delete account for cleanup
    signup.delete_account()
    assert signup.account_deleted()