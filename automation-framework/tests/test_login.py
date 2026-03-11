from pages.login_page import LoginPage

def test_invalid_login(page, user_data):

    login = LoginPage(page)

    login.load()

    login.login(user_data["email"], user_data["password"])

    assert login.error_visible()