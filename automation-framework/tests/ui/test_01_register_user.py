from utils.user_factory import generate_user
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Signup / Login' button
# 5. Verify 'New User Signup!' is visible
# 6. Enter name and email address
# 7. Click 'Signup' button
# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
# 9. Fill details: Title, Name, Email, Password, Date of birth
# 10. Select checkbox 'Sign up for our newsletter!'
# 11. Select checkbox 'Receive special offers from our partners!'
# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
# 13. Click 'Create Account button'
# 14. Verify that 'ACCOUNT CREATED!' is visible
# 15. Click 'Continue' button
# 16. Verify that 'Logged in as username' is visible
# 17. Click 'Delete Account' button
# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

def test_register_user(page):

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