from pages.home_page import HomePage
from pages.products_page import ProductsPage

# 1. Launch browser
# 2. Navigate to url 'http://automationexercise.com'
# 3. Verify that home page is visible successfully
# 4. Click on 'Products' button
# 5. Verify user is navigated to ALL PRODUCTS page successfully
# 6. Enter product name in search input and click search button
# 7. Verify 'SEARCHED PRODUCTS' is visible
# 8. Verify all the products related to search are visible
def test_search_product(page):

    home = HomePage(page)
    products = ProductsPage(page)

    # Launch browser and assert visibility
    home.load()
    assert home.home_visible()

    # Click 'Products' button
    home.go_to_products()

    # Verify user is navigated to ALL PRODUCTS page successfully
    products.verify_all_products_page()

    # Enter product name in search input and click search button
    products.search_product("Dress")

    # Verify 'SEARCHED PRODUCTS' is visible
    products.verify_searched_products_visible()

    # Verify all the products related to search are visible
    assert products.search_results_visible()