from playwright.sync_api import Page
from pages.home_page import AmazonHomePage

def test_amazon_search(page: Page):
    home_page = AmazonHomePage(page)

    home_page.navigate()
    home_page.get_title()

    home_page.search_for_product("iPhone")
    pass