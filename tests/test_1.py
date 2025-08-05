from selenium import webdriver
import time
from pages.main_page import MainPage
from pages.outdoor_page import OutdoorPage
from filters.filters import FilterPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from base.base_class import Base
from selenium.webdriver.chrome.options import Options

"""Тест"""

def test_perehod_catalog():
    
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    main_page = MainPage(driver)
    outdoor_page = OutdoorPage(driver)
    filters = FilterPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    base = Base(driver)


    main_page.catalog()
    outdoor_page.choose_tents()

    filters.apply_cookies()
    filters.filter_price()
    filters.filter_tourist_tent()
    filters.apply_filter()
    
    discount_price = products_page.save_discount_price_product1()
    name_product = products_page.save_name_product1() + ' (uni: one size)'

    products_page.add_to_cart_product1()

    final_price = cart_page.save_final_price_product1()
    final_name = cart_page.save_final_name() 
    
    assert discount_price == final_price, 'Цена не равна финальной цене!'
    print('Цены совпадают!')

    assert name_product == final_name, 'Наименования не совпадают!'
    print('Наименования совпадают!')

    base.get_screenshot()
    
    time.sleep(5)
    driver.quit()