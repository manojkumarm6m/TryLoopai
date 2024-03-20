# This page helps to store the selenium action methods like Click, enter, Select etc

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains

wait = 10


class Actions:
    def click_element(self, locator, value):
        try:
            element = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((locator, value)))
            element.click()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def enter_data(self, locator, value, input_key):
        try:
            element = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((locator, value)))
            element.clear()
            element.send_keys(input_key)
        except Exception as e:
            print(f"An error occurred: {e}")

    def retrieve_text(self, locator, value):
        try:
            element = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((locator, value)))
            return element.text
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def element_displayed(self, locator, value):
        try:
            element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((locator, value)))
            return element
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def multiple_elements(self, locator, value):
        try:
            elements = WebDriverWait(self.driver, wait).until(EC.presence_of_all_elements_located((locator, value)))
            return elements
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def click_on_previous(self, locator):
        try:
            element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))
            while element.is_enabled():
                ActionChains(self.driver).move_to_element(element).perform()
                element.click()
        except TimeoutException:
            print("Element not found within the given timeout.")

    def wait_for_element_and_hover(self, locator):
        try:
            element = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(locator))

            # Perform mouse hover over the element
            ActionChains(self.driver).move_to_element(element).perform()

            if element.is_enabled():
                return element
            else:
                return None

        except TimeoutException:
            print("TimeoutException: Element not clickable within the specified time frame.")
            return False