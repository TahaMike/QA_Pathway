from pages.base_page import BasePage

class ProductDetailsPage(BasePage): #PDP
    def __init__(self, page):
        super().__init__(page)

        # All those details attributes must be defined here like product title, price, storage, and other specific details
        self._product_title = page.locator("#productTitle")
        self._whole_price = page.locator(".a-whole-price").first
        self._fraction_price = page.locator(".a-fraction-price").first
        
    def verify_product_details(self):
        product_title = self._product_title
        print(f"{product_title} is loaded")
        pass