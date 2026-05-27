from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utils.user_factory import generate_user


def test_register_before_checkout(page):

    home = HomePage(page)
    login = LoginPage(page)
    signup = SignupPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    user = generate_user()

    # 1–2. Launch browser and navigate to home page
    home.load()

    # 3. Verify home page is visible
    assert home.home_visible()

    # 4. Navigate to Signup / Login page
    home.go_to_signup_login()

    # 5. Start signup and complete account creation
    login.start_signup(user["name"], user["email"])

    assert signup.account_form_visible()

    signup.complete_account_creation(user)

    # 6. Verify account created and continue
    assert signup.account_created()

    signup.click_continue()

    # 7. Verify logged in as username
    login.wait_for_login_success()

    assert login.logged_in_visible()

    # 8. Add product to cart
    home.go_to_products()

    products.add_first_product()

    # 9. Open cart page
    products.view_cart()

    # 10. Verify cart page contains items
    assert cart.cart_has_items()

    # 11. Proceed to checkout
    checkout.proceed_to_checkout()

    # 12. Verify checkout page sections
    assert checkout.checkout_page_visible()

    # 13. Enter order comment and place order
    checkout.enter_order_comment("Test order comment")

    checkout.place_order()

    # 14. Fill payment information
    checkout.fill_payment_details()

    # 15. Confirm payment
    checkout.pay_and_confirm_order()

    # 16. Verify successful order placement
    checkout.wait_for_order_success()

    assert checkout.order_success_visible()

    # 17. Delete account
    signup.delete_account()

    # 18. Verify account deleted and continue
    assert signup.account_deleted()

    signup.click_continue()