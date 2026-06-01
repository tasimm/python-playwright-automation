from pages.home_page import HomePage
from pages.category_page import CategoryPage


def test_view_category_products(page):

    home = HomePage(page)
    category = CategoryPage(page)

    # 1–2. Launch browser and navigate to home page
    home.load()

    # 3. Verify categories are visible
    assert category.categories_visible()

    # 4. Click Women category
    category.open_women_category()

    # 5. Click Dress sub-category
    category.open_women_dress_category()

    # 6. Verify category page is displayed
    category.category_page_visible()
    assert "WOMEN" in category.get_category_title()

    # 7. Click Men category
    category.open_men_category()

    # 8. Click Men sub-category
    category.open_men_tshirts_category()

    # Verify navigation occurred
    category.category_page_visible()
    assert "MEN" in category.get_category_title()