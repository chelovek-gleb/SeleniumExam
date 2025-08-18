import time
from pages.main_page import MainPage
from pages.outdoor_page import OutdoorPage
from filters.filters import FilterPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from base.base_class import Base
from selenium.webdriver.chrome.options import Options

"""Тест"""

def test_perehod_catalog(browser):
   
    """Объявление экземпляров класса"""
    main_page = MainPage(browser)
    outdoor_page = OutdoorPage(browser)
    filters = FilterPage(browser)
    products_page = ProductsPage(browser)
    cart_page = CartPage(browser)
    base = Base(browser)
    print(f'Размер окна браузера: {browser.get_window_size()}') # принт


    main_page.catalog() #Переходим в каталог
    outdoor_page.choose_tents() #Выбираем палатки и тенты

    filters.apply_cookies() # Подтверждаем куки
    filters.filter_price() # Фильтруем цены
    filters.filter_tourist_tent() #Фильтруем палатки Туристические
    filters.apply_filter() # Подтверждаем фильтры
    
    discount_price = products_page.save_discount_price_product1() # Сохранили цену по скидке
    name_product = products_page.save_name_product1() + ' (uni: one size)' # Сохранили наименование товара + размер

    products_page.add_to_cart_product1() # Добавили в корзину товар

    final_price = cart_page.save_final_price_product1() # Сохранили финальную цену из корзины
    final_name = cart_page.save_final_name()  # Сохранили финальное наименование из сорзины
    
    assert discount_price == final_price, 'Цена не равна финальной цене!'
    print('Цены совпадают!')

    assert name_product == final_name, 'Наименования не совпадают!'
    print('Наименования совпадают!')

    base.get_screenshot()
    
    time.sleep(5)
    