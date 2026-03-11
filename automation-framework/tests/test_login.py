from pages.login_page import LoginPage

def test_invalid_login(page):

    login = LoginPage(page)

    login.load()

    login.login("fake@email.com", "wrongpassword")

    #assert login.error_visible()
    assert False