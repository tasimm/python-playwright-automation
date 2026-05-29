from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.signup_page import SignupPage

def test_login_before_checkout(page):

    home = HomePage(page)
    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    signup = SignupPage(page)

    # Constant test user for login
    email = "test123user123@test.com"
    password = "password123"

    # 1–2. Launch browser and navigate to home page
    home.load()

    # 3. Verify home page is visible
    assert home.home_visible()

    # 4. Click Signup / Login
    home.go_to_signup_login()

    # 5. Login with existing account
    login.login(email, password)

    # 6. Verify user logged in
    login.wait_for_login_success()
    assert login.logged_in_visible()

    # 7. Add product to cart
    home.go_to_products()
    products.add_first_product()

    # 8. Click Cart
    products.view_cart()

    # 9. Verify cart page displayed
    assert cart.cart_has_items()

    # 10. Proceed to checkout
    checkout.proceed_to_checkout()

    # 11. Verify Address Details and Review Your Order
    assert checkout.checkout_page_visible()

    # 12. Enter comment and place order
    checkout.enter_order_comment(
        "Automated order created during Playwright test."
    )

    checkout.place_order()

    # 13. Enter payment details
    checkout.fill_payment_details()

    # 14. Pay and confirm order
    checkout.pay_and_confirm_order

    # 15. Verify successful order placement
    checkout.wait_for_order_success()
    assert checkout.order_success_visible()

    # 16. Delete account
    signup.delete_account()

    # 17. Verify account deleted and continue
    assert signup.account_deleted()

    signup.click_continue()