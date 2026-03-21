import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("name,email", [
    ("", ""),                    # both empty
    ("Test User", ""),           # missing email
    ("", "test@email.com"),      # missing name
    ("Test User", "invalid"),    # invalid email
])

def test_signup_invalid_inputs(page, name, email):

    login = LoginPage(page)

    login.load()
    login.start_signup(name, email)

    assert "login" in page.url