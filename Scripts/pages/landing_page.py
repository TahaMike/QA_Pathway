from playwright.sync_api import Page
from config import AppEndpoints

class LetterDraftingLandingPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators for the landing page buttons
        self._login_nav_button = self.page.get_by_role("link", name="Login")
        self._get_started_button = self.page.get_by_role("button", name="Get Started")

    def navigate(self):
        self.page.goto(AppEndpoints.BASE_URL, wait_until="domcontentloaded")

    def click_login(self):
        self._login_nav_button.click()