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












# from playwright.sync_api import sync_playwright
# from pages.login_page import LetterDaftingLoginPage
# from config import AppEndpoints

# from pathlib import Path


# def test_login():
#     root_path = Path(__file__).resolve().parent.parent
#     auth_path = root_path / "artifacts" / "auth_session.json"


#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless= False)
#         context = browser.new_context()
#         page = context.new_page()


#         login_page = LetterDaftingLoginPage(page)

#         try:
#             login_page.navigate()
#             login_page.try_login(username= AppEndpoints.USERNAME, password= AppEndpoints.PASSWORD)

#             context.storage_state(path= str(auth_path))

#         except Exception as e:
#             print(f"Test Execution failed: {e}")
#             raise e
        
#         finally:
#             context.close()
#             browser.close()