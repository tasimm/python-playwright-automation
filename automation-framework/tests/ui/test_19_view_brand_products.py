from pages.products_page import ProductsPage
from pages.category_page import CategoryPage

def test_view_brand_products(page):

    products = ProductsPage(page)
    category = CategoryPage(page)

    # 1–3. Launch browser and navigate to Products page
    products.load()

    # 3. Verify categories are visible
    assert category.brand_page_visible()

    # 5. Click on an brand name
    category.click_polo_brand()

    # 6. Verify that user is navigated to brand page and brand products are displayed
    assert category.polo_brand_page_visible()

    # 7. On left side bar, click on any other brand link
    category.click_hnm_brand()

    # 8. Verify that user is navigated to that brand page and can see products
    assert category.hnm_brand_page_visible()