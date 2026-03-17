from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def test_add_product_to_cart(page):

    products = ProductsPage(page)
    cart = CartPage(page)

    products.load()

    products.add_first_product_to_cart()

    products.view_cart()

    assert cart.cart_has_items()