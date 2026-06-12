from playwright.sync_api import Page

class QuickLettersPage:
    def __init__(self, page: Page):
        self.page = page
        # The root element where the app is injected
        self.root_container = page.locator("#root")
        
    def navigate(self):
        self.page.goto("https://letter-drafting.vercel.app/")

    def is_app_loaded(self) -> bool:
        # Check if the root has content (meaning React has mounted)
        return self.root_container.is_visible() and self.root_container.inner_html() != ""