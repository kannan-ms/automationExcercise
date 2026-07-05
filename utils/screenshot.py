from datetime import datetime
from pathlib import Path


def save_failure_screenshot(driver, test_name):
    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = test_name.replace("/", "_").replace("::", "_")
    screenshot_path = screenshots_dir / f"{safe_name}_{timestamp}.png"
    driver.save_screenshot(str(screenshot_path))
    return str(screenshot_path)
