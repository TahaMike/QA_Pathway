from playwright.sync_api import Page
from pages.home_page import AmazonHomePage
from pages.results_page import SearchResultPage

def test_amazon_search(page: Page):
    home_page = AmazonHomePage(page)
    result_page = SearchResultPage(page)

    home_page.navigate()
    home_page.get_title()

    home_page.search_for_product("iphone")


    result_page.verify_results_are_visible()

    product_details_tab = result_page.click_first_product_title()

    print(f"New Tab Title is: {product_details_tab.title()}")
    