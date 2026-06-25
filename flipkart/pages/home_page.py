from config import AppEndpoint
from playwright.sync_api import Page, Expect

class FlipKartHomePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(AppEndpoint.FLIPKART_BASE_URL)

    # def 