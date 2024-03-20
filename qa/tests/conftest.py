# In conftest file we add set up and tear down methods
import pytest
import allure
import time
from allure_commons.types import AttachmentType
from selenium import webdriver
from qa.utilities import ReadConfigurations
import chromedriver_autoinstaller
import geckodriver_autoinstaller
import edgedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

driver = None


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    global driver
    if browser.__eq__("chrome"):
        chromedriver_autoinstaller.install()
        driver = webdriver.Chrome()
    elif browser.__eq__("chrome-headless"):
        chromedriver_autoinstaller.install()
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser.__eq__("firefox"):
        geckodriver_autoinstaller.install()
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        edgedriver_autoinstaller.install()
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    app_url = ReadConfigurations.read_configuration("basic info", "app_url")
    driver.get(app_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed or (hasattr(item, "_evalskip") and item._evalskip):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"failed_test_{timestamp}.png"
        allure.attach(driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
