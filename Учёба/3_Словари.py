# slovar1 = {
#     'key1': 50,
#     'key2': 'xyi'
# }
#
# slovar2 = {
#     'key2': 'xyi',
#     'key1': 50
# }
# print(slovar1['key1'])
# print(slovar1 == slovar2)    #порядок параметров не важен в словаре
#
# """Изменение и удаление значений в словарях"""
# slovar3 = {
#     'key1': 50,
#     'key2': 'xyi'
# }
# slovar3['key1'] = 40   # изменил
# slovar3['key3'] = 777   # добавил
# del slovar3['key2'] #   удаление
# print(slovar3)
#
# """Использование переменных в словарях и вложенные словари, метод get"""
# price = 50
# organ = 'xyi'
# slovar5 = {
#     'key1': price,
#     'key2': organ,
#     'key3': {
#         'price': 40,
#         'dostup': True
#     }
# }
#
# key_name = 'key2'
# slovar5[key_name] = 'pisun'
#
# print(slovar5['key3']['price'])
# print(slovar5)
# print(len(slovar5))   # Длина списка
# print(slovar5.get('zdarova', 0))   # получаем значения ключа (0) в словаре которого нет
# print(slovar5.get('key2'))   # получаем значения ключа в словаре (которое есть)
# print(slovar5.items())
#
# """Копирование списка"""
# slovar6 = slovar5.copy()   # копирование списка
# slovar6['key4'] = 'German'
# print(slovar6)
#
# """Конвертация других значений в словарь"""
# spisok1 = [['lolo', 5], ['lialia', 7]]
# my_dict = dict(spisok1)   # из списка списков делаем словарь
# print(my_dict)
# """Задание"""
# moi_slovar = {}
#
# key_1 = input("Введите название ключа 1: ")
# value_1 = input("Введите значение 1: ")
# moi_slovar[key_1] = value_1
#
# key_2 = input("Введите название ключа 2: ")
# value_2 = input("Введите значение 2: ")
# moi_slovar[key_2] = value_2
#
# key_3 = input("Введите название ключа 3: ")
# value_3 = input("Введите значение 3: ")
# moi_slovar[key_3] = value_3
#
# print(moi_slovar)
#
# del moi_slovar[key_3]
# moi_slovar['key_status'] = 'Rich'
#
# print(moi_slovar)

"""Задание заполнение словаря через цикл for"""
moi_slovar1 = {}
n = int(input('Введите количество элементов в словаре: '))
for i in range(n):
    key = input(f"Введите ключ для элемента {i+1}: ")
    value = input(f"Введите значение для ключа {key}: ")
    moi_slovar1[key] = value
print(moi_slovar1)


