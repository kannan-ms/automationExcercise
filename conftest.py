import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.screenshot import save_failure_screenshot


@pytest.fixture
def driver():
    Path("reports").mkdir(parents=True, exist_ok=True)
    Path("screenshots").mkdir(parents=True, exist_ok=True)

    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or report.passed:
        return

    driver = item.funcargs.get("driver")
    if driver:
        save_failure_screenshot(driver, item.nodeid)