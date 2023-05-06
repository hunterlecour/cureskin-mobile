from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import Page


class Main(Page):
    TERMS_OF_SERVICE = (By.CSS_SELECTOR, 'a[href="/policies/terms-of-service"]')
    TERMS_OF_SERVICE_TITLE = (By.CSS_SELECTOR, 'div.shopify-policy__title')
    SHOP_BY_PRODUCT = (By.XPATH, '//span[text()="Shop by Product" and @class="menu-drawer__menu-item list-menu__item animate-arrow focus-inset"]')
    SHOP_BY_CATEGORY = (By.XPATH, '//span[contains(text(), "Shop by Category") and @class="menu-drawer__menu-item list-menu__item animate-arrow focus-inset"]')
    BODY_BUTTON = (By.XPATH, '//a[@href="/collections/body" and @class="menu-drawer__menu-item list-menu__item focus-inset"]')
    FACE_BUTTON = (By.XPATH, '//a[@href="/collections/face" and @class="menu-drawer__menu-item list-menu__item focus-inset"]')
    FACE_WASHES_BUTTON = (By.XPATH, '//a[@href="/collections/face-wash" and @class="menu-drawer__menu-item list-menu__item focus-inset"]')
    FACE_WASH_VERIFICATION = (By.CSS_SELECTOR, 'label[for="Filter-Product type-1"]')
    SUNSCREENS_BUTTON = (By.XPATH, '//a[@href="/collections/sun-protection" and @class="menu-drawer__menu-item list-menu__item focus-inset"]')
    SUNSCREEN_PRODUCT = (By.XPATH, '//a[contains(text(), "SPF30 Sunscreen")]')
    SUNSCREEN_PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product__title h1.h2')
    FACE_PRODUCT = (By.XPATH, '//a[contains(text(), "Gentle Cleanse Face Foam")]')
    FACE_PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product__title')
    POP_UP_CLOSE = (By.XPATH, "//button[@class='popup-close']")
    OUR_POLICIES = (By.XPATH, "//h2[contains(text(), 'Our policies')]")
    HAMBURGER_MENU = (By.CSS_SELECTOR, 'details.menu-drawer-container')

    def open_main_page(self):
        self.open_url('https://shop.cureskin.com/')
        self.wait_for_element_click(*self.POP_UP_CLOSE)

    def click_on_tos(self):
        self.wait_for_element_click(*self.OUR_POLICIES)
        self.wait_for_element_click(*self.TERMS_OF_SERVICE)

    def hamburger_menu(self):
        self.wait_for_element_click(*self.HAMBURGER_MENU)

    def click_shop_by_prod(self):
        self.wait_for_element_click(*self.SHOP_BY_PRODUCT)

    def click_on_face_washes(self):
        self.wait_for_element_click(*self.FACE_WASHES_BUTTON)

    def click_on_sunscreens(self):
        self.wait_for_element_click(*self.SUNSCREENS_BUTTON)

    def click_sunscreen_product(self):
        self.click(*self.SUNSCREEN_PRODUCT)

    def click_on_face(self):
        self.wait_for_element_click(*self.FACE_BUTTON)

    def click_on_shop_by_cat(self):
        self.click(*self.SHOP_BY_CATEGORY)

    def click_on_first_face_product(self):
        self.click(*self.FACE_PRODUCT)

    def click_on_body(self):
        self.wait_for_element_click(*self.BODY_BUTTON)

    def verify_tos_opens(self, text):
        self.verify_element(text, *self.TERMS_OF_SERVICE_TITLE)

    def verify_face_wash_shown(self, text):
        self.verify_element(text, *self.FACE_WASH_VERIFICATION)

    def verify_first_product_sunscreen(self, text):
        self.verify_element(text, *self.SUNSCREEN_PRODUCT_TITLE)

    def verify_on_face_page(self, text):
        self.verify_url(text)

    def verify_face_product_title(self, text):
        actual_description = self.driver.find_element(*self.FACE_PRODUCT_TITLE).text

        assert text in actual_description, f"Face is not in product description"








