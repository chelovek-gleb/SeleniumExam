import datetime
import os

"""Общие методы для всех страниц"""

class Base():

    def __init__(self, driver):
        self.driver = driver
        
    """Получаем текущий урл"""
    def get_current_url(self):
        get_url = self.driver.current_url
        return get_url

    """Проверяем какой-либо текст"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, 'Values not equal!!!'
        print('Good value word')

    """Метод скриншота"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot{now_date}.png'
        # папка для скринов в корне проекта
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        
        path = os.path.join(screenshots_dir, name_screenshot)
        self.driver.save_screenshot(path)
        print(f'Скриншот выполнен: {path}')

    """Проверка урла"""
    def assert_url(self, result):
        url = self.driver.current_url
        print('url= ', url)
        print('result= ', result)
        assert url == result, 'Урлы не совпадают!'
        print('Урлы совпадают!')