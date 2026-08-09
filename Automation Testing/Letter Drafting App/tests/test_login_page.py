import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from config import AppEndpoints

def test_user_can_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.navigate()
        
        # Monitor the network request
        with page.expect_response("**/auth/login") as response_info:
            login_page.login(AppEndpoints.USERNAME, AppEndpoints.PASSWORD)
        
        response = response_info.value
        assert response.status == 201
        
        # Verify token exists in response body
        body = response.json()
        assert "access_token" in body
        
        browser.close()


