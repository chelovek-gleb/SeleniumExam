from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger
import time
from selenium.common.exceptions import TimeoutException

"""Главная страница сайта"""

class MainPage(Base):
    
    url = 'https://www.kant.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    catalog_locator = '//a[@href="/catalog/"]' 
    tourism_and_camping_locator = '//a[@href="/catalog/outdoor/"]' # Туризм и кемпинг локатор
    notice_locator = '//div[@class="popmechanic-close"]' # локатор кнопки закрытия на уведомлении


    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.catalog_locator)))
    
    def get_tourism_and_camping(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.tourism_and_camping_locator)))
    
    def get_notice(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.notice_locator)))
    
    
    # Actions
    """Методы кликов на каталог, туризм и закрытие уведомления"""
    def click_catalog(self):
        self.close_notice_if_present()
        self.get_catalog().click()
        print('Кликнули на каталог')

    def click_tourism_and_camping(self):
        self.close_notice_if_present()
        self.get_tourism_and_camping().click()
        print('Кликнули на меню туризм и кемпинг')

    def click_close_notice(self):
        self.get_notice().click()
        print('Кликнули на закрытие уведомлений')

    def close_notice_if_present(self):
        """Метод закрытия уведомлений"""
        try:
            notice = WebDriverWait(self.driver, 45).until(EC.element_to_be_clickable((By.XPATH, self.notice_locator)))
            notice.click()
            print("Уведомление закрыто")
        except TimeoutException:
            print("Уведомление не появилось")
        except Exception as e:
            print(f"Ошибка при закрытии уведомления: {e}")


    # Methods
    def catalog(self):
        """Метод перехода с главной страницы в каталог и далее в раздел Туризм и кемпинг"""
        Logger.add_start_step(method = 'catalog')
        self.driver.get(self.url)
        self.click_catalog()
        time.sleep(5)
        self.click_tourism_and_camping()
        time.sleep(5)
        Logger.add_end_step(url = self.get_current_url, method='catalog')
    

  
