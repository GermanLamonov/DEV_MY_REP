"""
    Кортежи изменять нельзя!!!
    Порядок в кортежах важен
"""
kortej = ('imia', 1, 3)
kortej1 = (1, 5)
kortej2 = kortej + kortej1    # Объеденение кортежей
print(kortej2)
print(kortej)
print(len(kortej))
# kortej[2] = 7  Ошибка, нельзя изменять кортеж так же и удалять

"""Кортеж словарей"""
users = (
    {
        'user_id': 15,
        'user_name': 'German'
    },
    {
        'user_id': 16,
        'user_name': 'Artem'
    }
)
print(users[1]['user_id'])
users[1]['user_id'] = 100   # Изменяемые объекты в кортежах можно изменять
print(users[1]['user_id'])

"""Конвертация кортежа в список(чтобы изменить кортеж)"""
kortej_my = (10, 20)
spisok_my = list(kortej_my)    # Кортеж в список
spisok_my.append(30)    # добавили элемент в список

print(spisok_my)

kortej_my2 = tuple(spisok_my)   # Список в кортеж

print(kortej_my2)