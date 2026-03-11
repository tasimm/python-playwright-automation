from pages.signup_page import SignupPage

def test_create_account(page, user_data):

    signup = SignupPage(page)

    signup.load()

    signup.start_signup(user_data["name"], user_data["email"])

    signup.complete_account_creation(user_data)

    assert signup.account_created()