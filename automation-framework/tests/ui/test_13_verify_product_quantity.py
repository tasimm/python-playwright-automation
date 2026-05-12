from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_verify_product_quantity_in_cart(page):
    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    # 1–2. Launch browser and navigate to home page
    home.load()

    # 3. Verify home page is visible
    assert home.home_visible()

    # 4. Open first product detail page
    products.click_first_view_product()

    # 5. Verify product detail page is visible
    products.verify_product_detail_page()

    # 6. Increase quantity to 4
    products.set_quantity(4)

    # 7. Add product to cart
    products.add_product_from_detail_page()

    # 8. Open cart page
    products.view_cart()

    # 9. Verify product quantity in cart
    assert cart.verify_product_quantity(4)