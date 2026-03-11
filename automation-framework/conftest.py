import pytest
import os
import time
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser, request):
    context = browser.new_context()
    page = context.new_page()

    yield page

    # Take screenshot if test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        os.makedirs("screenshots", exist_ok=True)

        timestamp = int(time.time())
        filename = f"screenshots/{request.node.name}_{timestamp}.png"

        page.screenshot(path=filename)

        print(f"\nScreenshot saved: {filename}")

    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)