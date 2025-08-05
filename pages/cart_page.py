from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

"""Страница корзины"""

class CartPage(Base):

    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    """Локаторы финальной цены и наименования"""
    final_price_locator = "//div[contains(@class, 'basket__sidebarLine--total')]//div[contains(@class, 'Value')]"
    final_name_locator = "//div[contains(@class, 'basketItem__title')]"

     # Getters

    def get_final_price(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.final_price_locator)))
    
    def get_final_name(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.final_name_locator)))
    
    # Actions

    

    # Methods
    """Методы сохраняющие финальную цену и наименование"""
    def save_final_price_product1(self):
        print('Сохраняем финальную цену товара')
        price = self.get_final_price().text
        print(f'Финальная цена товара: {price}')
        return price
    
    def save_final_name(self):
        print('Сохраняем финальную цену товара')
        name = self.get_final_name().text
        print(f'Финальное наименование товара: {name}')
        return name