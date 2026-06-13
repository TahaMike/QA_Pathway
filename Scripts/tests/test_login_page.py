import pytest
from pathlib import Path
from pages.login_page import LoginPage

def test_login(page):
    """Validates the standard login process using injected page fixtures."""
    # Dynamically find the path to save your session state
    root_path = Path(__file__).resolve().parent.parent
    auth_path = root_path / "artifacts" / "auth_session.json"
    auth_path.parent.mkdir(parents=True, exist_ok=True)

    # Initialize the page object model layer
    login_page = LoginPage(page)
    
    try:
        login_page.navigate()
        login_page.try_login("leavoter9@gmail.com", "Taha@707")
        
        # Save the authenticated state for downstream regression tests
        page.context.storage_state(path=str(auth_path))
        print(f"Authentication token safely cached at: {auth_path}")
        
    except Exception as error:
        print(f"Test Assertion Error: {error}")
        raise error







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