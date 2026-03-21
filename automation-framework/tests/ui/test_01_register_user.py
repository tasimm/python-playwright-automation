from utils.user_factory import generate_user
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage

# Registers a new user account and then deletes account
def test_01_register_user(page):

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

    # Verify account form
    assert signup.account_form_visible()

    # Fill form + submit
    signup.complete_account_creation(user)

    # Verify account was created
    assert signup.account_created()

    # Click continue
    signup.click_continue()

    # Verify logged in
    assert login.logged_in_visible()

    # Delete account
    signup.delete_account()

    # Verify account deleted
    assert signup.account_deleted()

    signup.click_continue()