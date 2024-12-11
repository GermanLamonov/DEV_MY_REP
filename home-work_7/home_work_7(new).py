import time
from functools import reduce

"""
Дан список чисел. С помощью map() получить список,
где каждое число из исходного списка переведено в строку.
Пример: на входе – [1, 2, 3], на выходе – [‘1’, ‘2’, ‘3’]
"""
print('Задание 1 \n')
spisok = [1, 5, 3]
print(f"Список чисел {spisok} в строке =  {list(map(lambda x: str(x), spisok))}")
print("________________________________________________________")

"""
Дан список чисел. С помощью filter() получить список
тех элементов из исходного списка, значение которых
больше 0.
"""
print('Задание 2 \n')
spisok = [1, -2, 3, 0, 0.1]
print(f"Из списка чисел {spisok}, больше нуля = {list(filter(lambda x: x > 0, spisok))}")
print("________________________________________________________")

"""
Дан список строк. С помощью filter() получить список
тех строк из исходного списка, которые являются
палиндромами (читаются в обе стороны одинаково, например,
’abcсba’)
"""
print('Задание 3 \n')
spisok = ['ebal', 'nah', 'qweewQ', 'cOOc', 'abba']


def palindrom(a):
    # Проверяю вне зависимости от больших букв

    a_lower = a.lower()
    return a_lower == a_lower[::-1]


print(f"Палиндромами из списка {spisok} являются {list(filter(palindrom, spisok))}")
print("________________________________________________________")

"""
Сделать декоратор, который измеряет время,
затраченное на выполнение декорируемой функции.
"""
print('Задание 4 \n')


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # записываем время до выполнения функции
        result = func(*args, **kwargs)  # выполняем саму функцию
        end_time = time.time()  # записываем время после выполнения функции
        execution_time = end_time - start_time  # вычисляем время выполнения
        print(f"Функция '{func.__name__}' выполнена за {execution_time:.6f} секунд.")
        return result

    return wrapper


# Пример использования декоратора

@measure_time
def slow_function():
    time.sleep(1.2)


slow_function()

print("________________________________________________________")
"""
Используя map() и reduce() посчитать площадь
квартиры, имея на входе характеристики комнат квартиры.
Пример входных данных:
rooms = [
{"name": ”Kitchen", "length": 6, "width": 4},
{"name": ”Room 1", "length": 5.5, "width": 4.5},
{"name": ”Room 2", "length": 5, "width": 4},
{"name": ”Room 3", "length": 7, "width": 6.3},
]
"""
print('Задание 5 \n')
rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]
plowad_komnati = (list(map(lambda x: x["length"] * x["width"], rooms)))
plowad_hati = reduce(lambda x, y: x + y, plowad_komnati)
print(f"Площадь сраной хаты = {plowad_hati} м. кв.")
input("Введите Enter для выхода\n")
