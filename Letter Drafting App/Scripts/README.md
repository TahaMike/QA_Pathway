# Letter Drafting Automation Framework

A scalable, high-velocity automation testing framework built using **Python** and **Playwright**. This repository demonstrates production-grade test automation principles, focusing on speed, resource optimization, and strict decoupling of test logic from the user interface.

---

## Core Architecture & Engineering Thinking

Instead of writing linear, fragile automation scripts, this framework was designed from the ground up with clean-code principles tailored for modern single-page applications (SPAs).

### 1. Isolated Page Object Model (POM)

The framework strictly decouples the UI layer from the execution layer:

* **The Page Layer (`/pages`):** Holds user-facing locators (leveraging Playwright's semantic `get_by_placeholder` and `get_by_role` APIs) and granular action methods. It contains **zero assertions**, serving purely as an interface repository.
* **The Test Layer (`/tests`):** Expresses pure business scenarios and execution flows. It contains **zero hardcoded selectors**, making scripts read like plain-English use cases while handling test assertions.

### 2. Strategic Stateful Authentication (Session Caching)

To bypass repetitive UI login sequences across a growing regression suite, this framework implements **State Storage Caching**. The authentication sequence runs once, captures cookies and local storage tokens, and dumps them into an isolated environment artifact (`auth_session.json`). Subsequent tests can inject this state to initiate pre-authenticated browser contexts, saving significant execution time and reducing authentication-server strain.

### 3. Smart Lifecycle & Navigation Management

Rather than relying on generic page load strategies that block execution threads waiting for unneeded images or tracking scripts, the framework utilizes `wait_until="domcontentloaded"`. It allows the engine to begin element interactions the exact millisecond the DOM tree is parsed, relying on Playwright’s native **Actionability/Auto-Waiting** mechanisms to safely execute inputs without flakiness.

---

## Engineering Challenges & Technical Resolutions

### Challenge 1: Avoidance of Runtime Attribute Errors in POM Classes

* **Context:** Initial iterations declared locator strategies dynamically inside separate action methods. This caused scoping issues where cross-method interactions resulted in runtime exceptions due to uninstantiated variables.
* **Resolution:** Consolidated all UI locator definitions strictly inside the class constructor (`__init__`). This ensures all element points are lazily bound to the active page context the exact moment the object is instantiated, ensuring stability during test execution steps.

### Challenge 2: Handling Resource Cleanups Safely

* **Context:** Manual control over starting and terminating browser instances (`context.close()`, `browser.close()`) leaves background processes hanging if a test experiences an unexpected infrastructure crash.
* **Resolution:** Wrapped critical setup stages inside Python's context managers (`with sync_playwright() as p:`) and structured robust `try-except-finally` blocks to guarantee hardware resources and open ports are explicitly recycled back to the system regardless of whether a test passes or fails.

---

## Project Directory Structure

```text
letter_drafting_automation/
│
├── pages/                       # Object Repository (Locators & System Actions)
│   ├── __init__.py
│   ├── login_page.py            # Interfaces with credentials entries & landing actions
│   └── letter_draft_page.py     # Manages application drafting workspaces
│
├── tests/                       # Test Suites (Validation & Assertions)
│   ├── __init__.py
│   └── test_login.py            # Validates session tracking and access flows
│
├── artifacts/                   # Framework generation storage
│   └── auth_session.json        # Cached browser security states (Git-ignored)
│
├── config.py                    # Global system variables and base application endpoints
├── pytest.ini                   # Shared test suite runner execution parameters
└── requirements.txt             # Project engine version requirements

```

---

## Setup and Execution Guide

Follow these steps to configure your environment and execute the automated test suites locally.

### Prerequisites

* Python 3.8 or higher installed on your system.

### 1. Clone and Install Dependencies

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/letter-drafting-automation.git
cd letter-drafting-automation

# Install Python package dependencies
pip install -r requirements.txt

# Download required native Playwright browser binaries
playwright install

```

### 2. Running the Test Suite

The project uses **Pytest** as its core runner engine. Execute tests using the following configurations depending on your debugging requirements:

* **Standard Headless Mode (Fastest Execution):**
```bash
pytest

```


* **Headed Mode (Visualizes Browser Interaction):**
```bash
pytest --headed

```


* **Target a Specific Browser Engine:**
```bash
pytest --browser firefox --headed

```


* **Parallel Execution Engine (Distribute across multiple CPU workers):**
```bash
pytest -n auto --headed

```
