from pages.products_page import ProductsPage

def tests_products_page_loads(page):

    products = ProductsPage(page)

    products.load()

    assert products.products_visible()

def test_product_search(page):
    
    products = ProductsPage(page)

    products.load()

    products.search_product("Tshirt")

    assert products.search_results_visible()