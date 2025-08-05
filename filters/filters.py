from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.main_page import MainPage

class FilterPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Locators

    filter_price_from_locator = "(//input[@type='number'])[1]"
    filter_price_to_locator = "(//input[@type='number'])[2]"
    filter_tourist_locator = '//span[text()="туристические"]'
    apply_button_locator = '//span[text()="Применить"]'
    apply_button_cookies_locator = '//span[text()="Согласен"]'
    raiting_locator = '//span[text()="Наш рейтинг:"]'
    kol_vo_locator = '//span[text()="Количество мест"]' #локатор нужен для того чтобы к нему навестись и не перекрывать нужный чекбокс

     # Getters

    def get_filter_price_from(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_from_locator)))
    
    def get_filter_price_to(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_to_locator)))
    
    def get_filter_tourist(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_tourist_locator)))
    
    def get_apply_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.apply_button_locator)))
    
    def get_apply_button_cookies(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.apply_button_cookies_locator)))
    
    def get_raiting(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.raiting_locator)))
    
    def get_kol_vo(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.kol_vo_locator)))
    
    # Actions

    def send_filter_price_from(self):
        self.get_filter_price_from().clear()
        self.get_filter_price_from().send_keys('15000')
        print('Заполнили цену ОТ')

    def send_filter_price_to(self):
        self.get_filter_price_to().clear()
        self.get_filter_price_to().send_keys('50000')
        print('Заполнили цену ДО')
    
    def click_filter_tourist(self):
        self.get_filter_tourist().click()
        print('Нажали на фильтр Туристические палатки')

    def click_apply_button(self):
        self.get_apply_button().click()
        print('Нажали применить фильтр')

    def click_apply_button_cookies(self):
        self.get_apply_button_cookies().click()
        print('Нажали принять кукис')

    # Methods
    def apply_cookies(self):
        self.click_apply_button_cookies()
        time.sleep(5)

    def filter_price(self):
        self.send_filter_price_from()
        self.send_filter_price_to()
        time.sleep(5)

    def filter_tourist_tent(self):
        print('Пытаемся нажать чекбокс Туристические')
        time.sleep(10)
        self.actions.move_to_element(self.get_kol_vo()).perform()
        print('Должны были двинуться вниз к чекбоксу')
        time.sleep(5)
        self.click_filter_tourist()
        time.sleep(5)

    def apply_filter(self):
        print('Пытаемся подтвердить фильтры')
        self.actions.move_to_element(self.get_raiting()).perform()
        self.click_apply_button()
        time.sleep(5)
