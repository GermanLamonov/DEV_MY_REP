"""
При конвертации zip объекта в список получается
список кортежей.
"""

fruits2 = ['apple', 'banana', 'orange']
price = [50, 70, 65]
dostypnost = [True, False, False]

fruits_to_zip = zip(fruits2, price, dostypnost)
print(type(fruits_to_zip))

fruits_to_list = list(fruits_to_zip)
print(fruits_to_list)
print("_________________________")

"""Конвертация zip объекта в словарь, допускается
только 2 аргумента"""
fruits2 = ['apple', 'banana', 'orange']
price2 = [50, 70, 65]

fruits_to_zip2 = zip(fruits2, price2)
print(type(fruits_to_zip2))

fruits_to_dict = dict(fruits_to_zip2)
print(fruits_to_dict)
