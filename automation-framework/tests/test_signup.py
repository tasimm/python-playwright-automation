from pages.signup_page import SignupPage

def test_start_signup(page, user_data):

    signup = SignupPage(page)

    signup.load()

    signup.start_signup(user_data["name"], user_data["email"])

    assert signup.account_form_visible