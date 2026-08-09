import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright_instance():
    """Initializes the core Playwright instance once for the entire test run."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    """Launches a single shared browser instance for the entire test session."""
    # Headless is set to True here because CI/CD pipelines require it.
    # To see it run locally, you can use the command-line flag: pytest --headed
    browser_instance = playwright_instance.chromium.launch(headless=False)
    yield browser_instance
    browser_instance.close()

@pytest.fixture(scope="function")
def page(browser):
    """Creates a fresh isolated browser context and page for every individual test function."""
    context = browser.new_context()
    page_instance = context.new_page()
    
    yield page_instance  # This is where your actual test runs
    
    # Teardown phase: Executes automatically after the test finishes or crashes
    context.close()