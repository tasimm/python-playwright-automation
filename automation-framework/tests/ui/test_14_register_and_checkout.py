from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage

from utils.user_factory import generate_user

def test_register_and_checkout(page):

    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    login = LoginPage(page)
    signup = SignupPage(page)

    user = generate_user()

    # 1–2 Launch browser, Navigate to URL
    home.load()

    # 3 Verify that home page is visible
    assert home.home_visible()

    # 4 Add products to cart
    home.go_to_products()
    products.add_first_product()

    # 5 Click 'Cart' button
    products.view_cart()

    # 6 Verify that cart page is displayed
    assert cart.cart_has_items()

    # 7 Click 'Proceed To Checkout'
    checkout.proceed_to_checkout()

    # 8 Click 'Register / Login' button
    checkout.click_register_login()

    # 9 Fill all details in Signup and create account
    login.start_signup(user["name"], user["email"])

    signup.account_form_visible()
    signup.complete_account_creation(user)

    # 10 Verify 'ACCOUNT CREATED!' and click 'Continue' button
    assert signup.account_created()
    signup.click_continue()

    # 11 Verify ' Logged in as username' at top
    login.wait_for_login_success()
    assert login.logged_in_visible()

    # 12 Click 'Cart' button
    home.go_to_cart()

    # 13 Click 'Proceed To Checkout' button
    checkout.proceed_to_checkout()

    # 14 Verify Address Details and Review Your Order
    assert checkout.checkout_page_visible()

    # 15 Enter description in comment text area and click 'Place Order'
    checkout.enter_order_comment("Test order comment")
    checkout.place_order()

    # 16 Enter payment details: Name on Card, Card Number, CVC, Expiration date
    checkout.fill_payment_details()

    # 17 Click 'Pay and Confirm Order' button
    checkout.pay_and_confirm_order()

    # 18 Verify success message 'Your order has been placed successfully!'
    checkout.wait_for_order_success()
    assert checkout.order_success_visible()

    # 19 Click 'Delete Account' button
    signup.delete_account()

    # 20 Verify 'ACCOUNT DELETED!' and click 'Continue' button
    assert signup.account_deleted()
    signup.click_continue()