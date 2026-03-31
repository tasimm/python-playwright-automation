from pages.home_page import HomePage
from pages.products_page import ProductsPage

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Products' button
# 5. Verify user is navigated to ALL PRODUCTS page successfully
# 6. The products list is visible
# 7. Click on 'View Product' of first product
# 8. User is landed to product detail page
# 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
def test_verify_products_page(page):

    home = HomePage(page)
    products = ProductsPage(page)

    # Launch browser and assert visibility
    home.load()
    assert home.home_visible()

    # Click 'Products' button
    home.go_to_products()

    # Verify user is navigated to ALL PRODUCTS page successfully
    products.verify_all_products_page()

    # Assert products list is visible
    assert products.products_visible()

    # Click on 'View Product' of first product
    products.click_first_view_product()

    # Verify user is landed to product detail page
    products.verify_product_detail_page()

    # Assert that product details are visible
    assert products.product_details_visible()