from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

"""Страница после применения фильтров где перечислены товары"""

class ProductsPage(Base):
    """Класс продуктов представленных на странице"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(driver)

    # Locators

    product1_locator = '(//div[@data-index="0"])[1]' #локатор для первого продукта в списке 
    add_to_cart_product1_locator = '(//span[text()="Добавить в корзину"])[1]' #кнопка добавить в корзину у продукта 1
    add_to_cart_choose_size_locator = '(//span[text()="Добавить в корзину"])[25]' #локатор корзины в самой модалке
    go_to_cart_locator = '(//div[text()="В корзине"])[2]' #локатор для перехода в корзину из модалки

    discount_price_product1_locator = "(//div[@data-index='0'])[1]//span[contains(@class, 'ProductCard_price--discount')]" #Локатор для скидочной цены товара
    name_product1_locator = "(//div[@data-index='0'])[1]//a[contains(@class, 'ProductCard_title')]" #локатор наименования товара

    # Getters

    def get_product1(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.product1_locator)))

    def get_add_to_cart_product1(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product1_locator)))
    
    def get_add_to_cart_choose_size(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_choose_size_locator)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_locator)))
    
    def get_discount_price_product1(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.discount_price_product1_locator)))
    
    def get_name_product1(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.name_product1_locator)))

    # Actions

    def click_add_to_cart_product1(self):
        self.get_add_to_cart_product1().click()
        print('Кликнули добавить в корзину')

    def click_add_to_cart_choose_size(self):
        self.get_add_to_cart_choose_size().click()
        print('Кликнули добавить в корзину при выборе размера')

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print('Кликнули перейти в корзину из модального окна')
        

    # Methods
    """Метод добавления товара в корзину"""
    def add_to_cart_product1(self):
        print('Нажимаем кнопку добавить в корзину')
        self.actions.move_to_element(self.get_product1()).perform() #Нужно навестись на товар чтобы появилась кнопка добавить в корзину
        time.sleep(3)
        self.click_add_to_cart_product1()
        time.sleep(3)
        print('Переходим в корзину из модалки')
        self.click_add_to_cart_choose_size()
        time.sleep(3)
        self.click_go_to_cart()
        time.sleep(3)

    """Метод сохраняющий скидочную цену товара"""
    def save_discount_price_product1(self):
        print('Сохраняем скидочную цену товара')
        price = self.get_discount_price_product1().text
        print(f'Цена товара по скидке: {price}')
        return price

    """Метод сохраняющий наименование товара"""    
    def save_name_product1(self):
        print('Сохраняем наименование товара')
        name = self.get_name_product1().text
        print(f'Наименование товара: {name}')
        return name