from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class Search_Result(Page):
    LOGO_HEADER = (By.XPATH, '//a[@class="header__heading-link focus-inset"]')
    PRODUCT_RESULTS = (By.ID, 'ProductCount')

    def open_search_result_cure(self):
        self.open_url('https://shop.cureskin.com/search?q=cure')

    def click_logo_header(self):
        self.click(*self.LOGO_HEADER)

    def verify_on_main_page(self, text):
        self.verify_url(text)

    def verify_23_products(self, text):
        self.verify_element(text, *self.PRODUCT_RESULTS)
