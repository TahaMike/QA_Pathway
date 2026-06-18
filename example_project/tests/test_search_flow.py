from playwright.sync_api import Page
from pages.home_page import AmazonHomePage
from pages.results_page import SearchResultPage
from pages.product_details_page import ProductDetailsPage

def test_amazon_search(page: Page):
    home_page = AmazonHomePage(page)
    result_page = SearchResultPage(page)
    product_page = ProductDetailsPage(page)

    home_page.navigate()
    home_page.get_title()

    home_page.search_for_product("iphone")


    result_page.verify_results_are_visible()

    product_details_tab = result_page.click_first_product_title()

    product_page.verify_product_details()
    
    print(f"New Tab Title is: {product_details_tab.title()}")
    