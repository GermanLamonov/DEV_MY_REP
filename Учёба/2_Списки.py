# posts_ids = [254, 244, 575, 686]
# print(posts_ids)
# print(len(posts_ids))
# posts_ids[2] = 777
# del posts_ids[3]
# print(posts_ids)
# print("___________________________________________________")
# users = [
#     {
#         'user_id': 17,
#         'user_name': 'German'
#     },
#     {
#         'user_id': 18,
#         'user_name': 'Kolia'
#     }
# ]
# print(f'Длина списка: {len(users)}')
# print(users[1]['user_id'])
# print("___________________________________________________")
# fruit_1 = 'banana'
# fruit_2 = 'apple'
# fruit_3 = 'orange'
# fruit_4 = 'lime'
# all_fruits = [fruit_1, fruit_2, fruit_3, fruit_4]
# all_fruits2 = []
# all_fruits2.append(fruit_4)
# all_fruits2.append(fruit_1)
# print(f'Список всех фруктов 1: {all_fruits}')
# print(f'Список всех фруктов 2: {all_fruits2}')
# del_first = all_fruits.pop(0) #присвоили удалённый элемент списка переменной
# print(f'Удалённый элемент из списка: {del_first}')
# print("___________________________________________________")
# posts_ids_1 = [2, 4, 12, 3]
# print(posts_ids_1)
# posts_ids_1.sort()  # сортировка списка
# print(f'Отсортиван по возрастанию: {posts_ids_1}')
# posts_ids_1.sort(reverse=True)  # сортировка по убыванию
# print(f'Отсортирован по убыванию: {posts_ids_1}')
# print("___________________________________________________")
# greeting = 'Zdarova Otec'
# greeting_letters = list(greeting)  # Конвертация строки в список
# print(greeting_letters)
# print("___________________________________________________")
# """Арифмитические операции в списке"""
# spisok1 = [5, 7.5, 8, 4.2]
# spisok2 = [1, 2, 6]
# spisok3 = spisok1 + spisok2   # сложили 2 списка в один
# print(spisok3)
# print(min(spisok1))
# print(max(spisok1))
# print(sum(spisok1))
# print(sum(spisok1)/len(spisok1))   # Сумму элементов списка разделили на его длину
# print("___________________________________________________")
# """Копирование списка"""
# spis = [3, 4]
# spis1 = spis.copy()   # копирование списка()
# spis1.append(5)
# print(spis)
# print(spis1)
# print(id(spis1) == id(spis))
# print("___________________________________________________")
# """Методы списка"""
# spis2 = [3, 4, 5, 0]
# spis2.insert(3, -4)   # добавление элемента в список перед указанным индексом
# print(spis2)
# spis2.extend('abc')    # расширили список
# print(spis2)
"""Задание 1"""
spisok = [1, 'German', 2.5, True, None]
spisok.pop(2)
print(len(spisok))
spisok.reverse()
spisok2 = [2, 'Dodik']
spisok.extend(spisok2)
print(spisok2)
print(spisok)
print("___________________________________________________")
"""Задание 2"""
spisok3 = [1, 2]
spisok4 = [3, 4]
spisok5 = spisok3 + spisok4
print(spisok3.__add__(spisok4))
print(spisok5)

