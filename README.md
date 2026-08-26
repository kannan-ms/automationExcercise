# Automation Exercise QA Automation Framework

This project is a Selenium-based UI automation framework created for the Automation Exercise web application.

The project uses Python, Selenium WebDriver, Pytest, and the Page Object Model design pattern. It focuses on automating common e-commerce workflows such as authentication, product validation, product search, adding products to cart, and removing products from cart.

Website under test: https://automationexercise.com/

## Tools and Technologies

* Python
* Selenium WebDriver
* Pytest
* Pytest HTML Reports
* Page Object Model
* Chrome Browser
* Git and GitHub

## Framework Features

* Page Object Model structure for reusable page actions
* Explicit waits for stable element interaction
* Separate page classes and test files
* Dynamic test user generation for login and logout flows
* Screenshot capture when a test fails
* HTML report generation after execution
* Independent test cases that can be run separately

## Project Structure

```text
automationExcercise/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── product_page.py
│   └── cart_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_authentication.py
│   ├── test_products.py
│   └── test_cart_phase1.py
│
├── test_data/
│   └── user_data.py
│
├── utils/
│   ├── __init__.py
│   ├── data_generator.py
│   └── screenshot.py
│
├── reports/
├── screenshots/
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Completed Test Scenarios

The following test cases are currently automated:

1. Login with correct email and password
2. Login with incorrect email and password
3. Logout user
4. Verify all products page and product details page
5. Search product
6. Add products to cart
7. Remove products from cart

## Test Execution

Run all Phase 1 tests:

```bash
pytest tests/test_authentication.py tests/test_products.py tests/test_cart_phase1.py -v
```

Run the complete test suite:

```bash
pytest -v
```

## Test Report

After execution, the HTML report is generated inside the `reports` folder.

Example:

```text
reports/phase1_report.html
```

Open the report in a browser to view test execution status, passed tests, failed tests, and execution details.

## Screenshot on Failure

The framework captures a screenshot automatically when a test fails.

Screenshots are stored inside:

```text
screenshots/
```

This helps to understand the browser state at the time of failure and makes debugging easier.

## Page Object Model Approach

The project follows the Page Object Model design pattern.

* `pages/` contains locators and actions related to each application page.
* `tests/` contains test scenarios and assertions.
* `base_page.py` contains reusable methods such as click, enter text, get text, and explicit wait handling.
* `conftest.py` handles browser setup, browser teardown, and screenshot capture on failure.

This structure keeps the test code clean and makes the framework easier to maintain.

## Sample Test Flow

Example flow for product search:

1. Open Automation Exercise home page
2. Navigate to the Products page
3. Enter a product name in the search field
4. Click the Search button
5. Verify that searched products are displayed

## How to Run the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the tests:

```bash
pytest -v
```

## Future Enhancements

The following scenarios are planned for the next phase:

* User registration
* Registration with existing email
* Contact Us form validation
* Subscription validation on home page and cart page
* Product quantity validation in cart
* Category and brand product validation
* Product review submission
* Recommended products validation
* Checkout flow and address validation


## About the Project

The test scenarios were selected from the functional flows available in Automation Exercise. The automation framework, page classes, reusable methods, test data handling, reports, and failure screenshot handling were implemented as part of this project to practice real QA automation framework structure.
