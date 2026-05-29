from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_remove_products_from_cart(page):

    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    # 1–2. Launch browser and navigate to home page
    home.load()

    # 3. Verify home page is visible
    assert home.home_visible()

    # 4. Add product to cart
    home.go_to_products()
    products.add_first_product()

    # 5. Click Cart button
    products.view_cart()

    # 6. Verify cart page is displayed
    assert cart.cart_has_items()

    # 7. Remove product from cart
    cart.remove_first_product()

    # 8. Verify product was removed
    assert cart.cart_empty()