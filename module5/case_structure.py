
"""
1. Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear). 
Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный код.
2. Нажимаем на кнопку "Добавить в корзину".
3. *Посчитать результат математического выражения и ввести ответ. Используйте для этого метод solve_quiz_and_get_code(), 
который приведен ниже. Например, можете добавить его в класс BasePage, чтобы использовать его на любой странице. Этот метод 
нужен только для проверки того, что вы написали тест на Selenium. После этого вы получите код, который нужно ввести в
качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. Не забудьте 
в конце теста добавить проверки на ожидаемый результат.

Ожидаемый результат: 

1. Сообщение о том, что товар добавлен в корзину. Название товара в сообщении 
должно совпадать с тем товаром, который вы действительно добавили.
2. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 
"""

# Структура авто-теста:

test_product_page.py #Сам тест
    """ - Функции описывающие шаги тест-кейса, с сылками на product_page и locators"""
__init__.py #Вспомогательный файл (пустой)
conftest.py #Базовый модуль с фикстурами (декораторы)
    """ - фикстура add_option добавляет доп. опции к драйверу"""
    """ - фикстура browser запускает браузер с заданными параметрами"""
pages >
    base_page.py #Описание общей функциональности страниц
        """ - функция __init__ задаёт драйвер, урл, время ожидания"""
        """ - функция open переходит по заданному урлу"""
        """ - фуркция проверки нахождения заданного элемента на странице"""
    product_page.py #Описание класса Page Object для страницы товара
        """ - Класс унаследованный от base_page"""
        """ - функции валидирующие элементы на странице и описание их взаимодействия"""
    locators.py #Описание локаторов
        """ - Переменные заключенные в Класс == Страница"""
    
