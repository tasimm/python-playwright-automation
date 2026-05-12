from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click 'Products' button
# 5. Hover over first product and click 'Add to cart'
# 6. Click 'Continue Shopping' button
# 7. Hover over second product and click 'Add to cart'
# 8. Click 'View Cart' button
# 9. Verify both products are added to Cart
# 10. Verify their prices, quantity and total price
def test_add_products_to_cart(page):

    home = HomePage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    # Launch browser and assert visibility
    home.load()
    assert home.home_visible()

    # Click 'Products' button
    home.go_to_products()

    # Hover over first product and click 'Add to cart'
    products.add_first_product()

    # Click 'Continue Shopping' button
    products.continue_shopping()

    # Hover over second product and click 'Add to cart'
    products.add_second_product()

    # Click 'View Cart' button
    products.view_cart()

    # Verify both products are added to Cart
    cart.verify_products_in_cart()
    assert cart.get_product_count() == 2

    # Verify their prices, quantity and total price
    assert cart.prices_visible()
    assert cart.quantity_visible()
    assert cart.total_visible()