from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, *locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def verify_element(self, text, *locator):
        expected_text = text
        actual_text = self.driver.find_element(*locator).text

        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_url(self, text):
        actual_url = self.driver.current_url
        expected_url = text
        assert actual_url == expected_url, f'expected{expected_url} but got {actual_url}'

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))