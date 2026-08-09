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




