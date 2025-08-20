from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time
from selenium.webdriver.common.action_chains import ActionChains

"""Класс фильтров. Все фильтры по товарам хранятся здесь"""

class FilterPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Locators

    filter_price_from_locator = "(//input[@type='number'])[1]" # фильтр цена ОТ
    filter_price_to_locator = "(//input[@type='number'])[2]" # фильтр цена ДО
    filter_tourist_locator = '//span[text()="туристические"]' # фильтр туристические палатки
    apply_button_locator = '//span[text()="Применить"]' # кнопка подтвердить фильтры
    apply_button_cookies_locator = '//span[text()="Согласен"]' #подтвердить куки
    raiting_locator = '//span[text()="Наш рейтинг:"]' #локатор нужен для того чтобы к нему навестись и нажать кнопку применить
    kol_vo_locator = '//span[text()="Количество мест"]' #локатор нужен для того чтобы к нему навестись и не перекрывать нужный чекбокс

     # Getters

    def get_filter_price_from(self): # фильтр цена ОТ
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_from_locator)))
    
    def get_filter_price_to(self): # фильтр цена ДО
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_to_locator)))
    
    def get_filter_tourist(self): # фильтр туристические палатки
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.filter_tourist_locator)))
    
    def get_apply_button(self): # кнопка подтвердить фильтры
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.apply_button_locator)))
    
    def get_apply_button_cookies(self): #подтвердить куки
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.apply_button_cookies_locator)))
    
    def get_raiting(self): #локатор нужен для того чтобы к нему навестись и нажать кнопку применить
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.raiting_locator)))
    
    def get_kol_vo(self): #локатор нужен для того чтобы к нему навестись и не перекрывать нужный чекбокс
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.kol_vo_locator)))
    
    # Actions
    """методы заполнения цены и кликов по кнопкам"""
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
    """Метод подтверждения куки"""
    def apply_cookies(self):
        self.click_apply_button_cookies()
        time.sleep(5)

    """Метод фильтрации цены"""
    def filter_price(self):
        self.send_filter_price_from()
        self.send_filter_price_to()
        time.sleep(5)


    """Метод фильтрации палаток по виду Туристические"""
    def filter_tourist_tent(self):
        print('Пытаемся нажать чекбокс Туристические')
        time.sleep(10)
        self.actions.move_to_element(self.get_kol_vo()).perform()
        print('Должны были двинуться вниз к чекбоксу')
        time.sleep(5)
        self.click_filter_tourist()
        time.sleep(5)

    """Метод подтверждения фильтра"""
    def apply_filter(self):
        print('Пытаемся подтвердить фильтры')
        self.actions.move_to_element(self.get_raiting()).perform()
        self.click_apply_button()
        time.sleep(5)
