from core.base_page import BasePage
from playwright.sync_api import expect

class CategoryPage(BasePage):

    # Headers
    CATEGORIES_HEADER = "h2:has-text('Category')"
    BRANDS_HEADER = "h2:has-text('Brands')"
    POLO_BRAND_HEADER = "h2:has-text('Brand - Polo Products')"
    HNM_BRAND_HEADER = "h2:has-text('Brand - H&M Products')"

    # Category subsections
    WOMEN_CATEGORY = "a[href='#Women']"
    WOMEN_DRESS_LINK = "a[href='/category_products/1']"

    MEN_CATEGORY = "a[href='#Men']"
    MEN_TSHIRTS_LINK = "a[href='/category_products/3']"

    # Brand subsections
    POLO_BRAND = "a[href='/brand_products/Polo']"
    HNM_BRAND = "a[href='/brand_products/H&M']"

    CATEGORY_TITLE = ".title.text-center"

    # ---------- CATEGORY NAVIGATION ----------
    
    def open_women_category(self):
        # Expand 'Women' Category section
        self.click(self.WOMEN_CATEGORY)

    def open_women_dress_category(self):
        # Open Women > Dress Category
        self.click(self.WOMEN_DRESS_LINK)

    def open_men_category(self):
        # Expand 'Men' Category section
        self.click(self.MEN_CATEGORY)

    def open_men_tshirts_category(self):
        # Open Men > Tshirts Category
        self.click(self.MEN_TSHIRTS_LINK)

    def click_polo_brand(self):
        # Expand 'Polo' Brand section
        self.click(self.POLO_BRAND)

    def click_hnm_brand(self):
        # Expand 'H&M' Brand section
        self.click(self.HNM_BRAND)

    # ---------- VALIDATION ----------

    def categories_visible(self):
        # Verify categories section is displayed
        return self.page.locator(self.CATEGORIES_HEADER).is_visible()

    def category_page_visible(self):
        # Verify category page header is visible
        expect(self.page.locator(self.CATEGORY_TITLE)).to_be_visible(timeout=5000)

    def get_category_title(self):
        # Return category page title text
        return self.page.locator(self.CATEGORY_TITLE).inner_text()
    
    def brand_page_visible(self):
        # Verify brand page header is visible
        return self.page.locator(self.BRANDS_HEADER).is_visible()

    def polo_brand_page_visible(self):
        # Verify brand page header is visible
        return self.page.locator(self.POLO_BRAND_HEADER).is_visible()

    def hnm_brand_page_visible(self):
        # Verify brand page header is visible
        return self.page.locator(self.HNM_BRAND_HEADER).is_visible()