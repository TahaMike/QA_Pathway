from pages.base_page import BasePage

class SearchResultPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self._search_results = page.locator(".s-result-item[data-asin]")

    def verify_results_are_visible(self):
        
        self._search_results = self.page.locator(".s-result-item[data-asin]").filter(has=self.page.locator("a.a-link-normal"))

    def click_first_product_title(self):
        
        first_product_card = self._search_results.filter(has_not_text="").first

        product_title_link = first_product_card.locator("a.a-link-normal h2").first


        with self.page.context.expect_page() as new_tab_info:
           
            product_title_link.click(force=True)

        new_tab = new_tab_info.value
        new_tab.wait_for_load_state("domcontentloaded")
        return new_tab

