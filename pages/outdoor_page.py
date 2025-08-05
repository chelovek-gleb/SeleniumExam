from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.main_page import MainPage
import time


"""Страница Туризм и кемпинг. Тут мы выбираем палатки и тенты"""

class OutdoorPage(Base):

    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    tents_locator = '//span[text()="Палатки и тенты"]'

     # Getters

    def get_tents(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.tents_locator)))
    
    # Actions

    def click_tents(self):
        self.get_tents().click()
        print('Кликнули на Палатки и тенты')

    # Methods

    def choose_tents(self):
        self.click_tents()
        time.sleep(5)