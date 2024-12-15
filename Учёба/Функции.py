# """Функция - это блок кода который можно выполнять
# многократно"""
#
#
# def my_fn(a, b):
#     return a + b
#
#
# x = int(input('Введи первое: '))
# y = int(input('Введи второе: '))
# result = my_fn(x, y)
# print(result)
# print("___________________________________________________")
#
#
# def sum_nums(a, b):
#     sui = a + b
#     return sui
#
#
# first_sum = sum_nums(5, 6)
# print(first_sum)
# second_sum = (sum_nums(sum_nums(50.7, 20.2), 30))
# print(second_sum)
# print(id(first_sum))

"""Задание"""

#
# def merge_lists_to_dict(list_1, list_2):
#     return dict(zip(list_1, list_2))
#
#
# result = merge_lists_to_dict(['Name', 'Age', 'Status'], ['German', 28, 'Krasavec'])
# print(result)

"""Аргументы функции задание"""


# def update_car_info(**car):
#     car['is_available'] = True
#     return car
#
#
# res = update_car_info(brand='Mers', price=100)
# print(res)
#
"""Колбэк функция"""


def print_number_info(num):
    if (num % 2) == 0:
        print("Введенное число чётное")
    else:
        print("Введенное число нечётное")


def print_square_number(num):
    print("Квадрат =", num * num)


def process_number(num, callback_fn):
    callback_fn(num)


entered_num = int(input('Введите цифру или число: '))
process_number(entered_num, print_number_info)
process_number(entered_num, print_square_number)

"""Создание глобальной переменной в функции
(не рекомендуетсядля изменения переменной)
dir() - чтобы узнать какие переменные доступны в области
"""


def my_fn():
    global a_glob
    a_glob = 10
    print(dir())


my_fn()
print(a_glob)

