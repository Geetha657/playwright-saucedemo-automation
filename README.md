PLAYWRIGHT UI AUTOMATION FRAMEWORK - SAUCEDEMO

PROJECT OVERVIEW

This project is a UI automation testing framework developed using Python, Playwright, and Pytest to test the SauceDemo e-commerce application.

The framework follows the Page Object Model (POM) design pattern to improve code reusability, maintainability, and scalability.

It includes automated functional, regression, positive, negative, and data-driven test scenarios covering important e-commerce workflows.

APPLICATION UNDER TEST

Application Name: SauceDemo

Website: https://www.saucedemo.com/

Application Type: E-commerce Web Application

TECHNOLOGIES USED

Programming Language: Python

Automation Tool: Playwright

Testing Framework: Pytest

Design Pattern: Page Object Model (POM)

Test Reporting: Pytest HTML

Version Control: Git and GitHub

Browsers: Chromium and WebKit

PROJECT STRUCTURE

playwright-saucedemo-tests/

pages/ - Contains reusable Page Object Model classes.

login_page.py - Handles login functionality and locators.

inventory_page.py - Handles product inventory, sorting, and cart operations.

cart_page.py - Handles shopping cart functionality.

checkout_page.py - Handles checkout and order completion.

test/ - Contains automated test scripts.

test_login.py - Login validation tests.

test_inventory.py - Product sorting tests.

test_cart.py - Shopping cart tests.

test_checkout.py - Checkout functionality tests.

conftest.py - Contains shared Pytest fixtures and setup.

pytest.ini - Contains Pytest configuration.

requirements.txt - Contains Python project dependencies.

.env - Stores local test configuration and credentials. Excluded from Git.

.gitignore - Specifies files excluded from version control.

README.md - Project documentation.

AUTOMATED TEST SCENARIOS

Login Testing

Valid login using correct credentials.

Invalid username validation.

Invalid password validation.

Empty username validation.

Empty password validation.

Inventory Testing

Product sorting by price from low to high.

Product sorting by price from high to low.

Product sorting by name from A to Z.

Product sorting by name from Z to A.

Shopping Cart Testing

Adding a product to the shopping cart.

Adding multiple products and removing a product.

Verifying product details in the shopping cart.

Checkout Testing

Successful checkout with valid customer information.

Checkout validation with missing first name.

Checkout validation with missing last name.

Checkout validation with missing postal code.

Total Automated Test Cases: 16

FRAMEWORK FEATURES

Page Object Model architecture for reusable automation code.

Pytest fixtures for test setup and authenticated sessions.

Parameterized tests for positive and negative scenarios.

Cross-browser testing using Chromium and WebKit.

HTML test execution reporting.

Environment-based test configuration.

Git-based source code management.

INSTALLATION AND SETUP

Step 1: Clone the GitHub repository.

git clone https://github.com/Geetha657/playwright-saucedemo-automation.git

Step 2: Navigate to the project directory.

cd playwright-saucedemo-automation

Step 3: Create a Python virtual environment.

python3 -m venv .venv

Step 4: Activate the virtual environment on macOS or Linux.

source .venv/bin/activate

Step 5: Install project dependencies.

python -m pip install -r requirements.txt

Step 6: Install Playwright browsers.

python -m playwright install chromium webkit

Step 7: Create a .env file in the project root with the following values.

BASE_URL=https://www.saucedemo.com/

USERNAME=standard_user

PASSWORD=secret_sauce

TEST EXECUTION

Run all automated tests:

python -m pytest test/ -v

Run tests using Chromium:

python -m pytest test/ --browser chromium -v

Run tests using WebKit:

python -m pytest test/ --browser webkit -v

Run tests across Chromium and WebKit:

python -m pytest test/ --browser chromium --browser webkit -v

GENERATE HTML TEST REPORT

Run the following command:

python -m pytest test/ --browser chromium --html=report.html --self-contained-html

Open the generated report on macOS:

open report.html

TEST EXECUTION STATUS

Automated Test Cases: 16

Test Modules: 4

Supported Test Execution Browsers: Chromium and WebKit

Firefox testing is currently excluded because of a local browser launch issue.

FUTURE ENHANCEMENTS

GitHub Actions CI/CD integration.

Improved test reporting and execution artifacts.

Additional end-to-end test scenarios.

Expanded cross-browser testing.

Parallel test execution.

AUTHOR

Geethanjali Vasa

QA Automation Engineer (SDET)

GitHub: https://github.com/Geetha657

LinkedIn: https://www.linkedin.com/in/geethanjali-vasa

PROJECT REPOSITORY

https://github.com/Geetha657/playwright-saucedemo-automation
