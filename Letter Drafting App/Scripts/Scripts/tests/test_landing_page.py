from playwright.sync_api import Page, expect
from pages.landing_page import LetterDraftingLandingPage
from config import AppEndpoints

def test_login_redirect(page: Page):
    landing_page = LetterDraftingLandingPage(page)
    
    landing_page.navigate()
    landing_page.click_login()
    
    # Assert that the URL successfully changed to the login page endpoint
    expect(page).to_have_url(AppEndpoints.LOGIN_PAGE)