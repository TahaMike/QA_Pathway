from config import AppEndpoints
from pages.base_page import BasePage

class AmazonHomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._searchbox = page.get_by_role("searchbox", name= "Search Amazon.in")
        self._search_button = page.get_by_role("button", name= "Go", exact= True)

    def search_for_product(self, product_name: str):
        self._searchbox.fill(product_name)
        self._search_button.click()

    def navigate(self):
        self.page.goto(AppEndpoints.BASE_URL, wait_until = "domcontentloaded")