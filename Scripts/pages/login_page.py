from config import AppEndpoints


class LoginPage:
    def __init__(self, page):
        self.page = page
        self._email = page.get_by_placeholder("you@company.com") # Adjust selectors to match your HTML
        self._password = page.get_by_placeholder("••••••••")
        self._login_button = page.get_by_role("button", name="Sign In")

    def navigate(self):
        self.page.goto(AppEndpoints.LOGIN_PAGE)

    def login(self, email, password):
        self._email.fill(email)
        self._password.fill(password)
        self._login_button.click()








# from playwright.sync_api import Page
# from config import AppEndpoints

# class LetterDaftingLoginPage:
#     def __init__(self, page: Page):
#         self.page = page

#         self._username = self.page.get_by_placeholder("you@company.com")
#         self._password = self.page.get_by_placeholder("••••••••")
#         self._login_button = self.page.get_by_role("button", name= "Sign In")


#     def navigate(self):
#         self.page.goto(AppEndpoints.LOGIN_PAGE, wait_until= "domcontentloaded")

       

#     def try_login(self, username: str, password: str):
#         try:
#             self._username.fill(username)
#             self._password.fill(password)
#             self._login_button.click()
#         except TimeoutError as te:
#             print(f"CRITICAL ERROR: Login elements failed to load or accept input. Details: {te}")
#             raise te
        

        

