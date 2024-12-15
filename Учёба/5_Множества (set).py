# """Набор - неупорядоченная последовательность элементов
#    Набор содержит только уникальные элементы
#    Набор обычно состоит из однотипных объектов!
#    У элементов наборы нету индекса!
#    Порядок в наборах не важен!
#    В наборы нельзя добавлять изменяемые объекты, только неизменяемые!
# """
# # nabor = {5, 5, 5, 1, 6}
# # print(nabor)
# # print(len(nabor))
# # nabor1 = set()    # Пустой набор
# # print(nabor1)
#
# """Методы наборов"""
# my_nabor = {5, 6}
# my_nabor2 = {5, 6, 7, 8}
# my_nabor.add(7)    # Добавление элемента в набор
# print(my_nabor)
# my_nabor3 = my_nabor.union(my_nabor2)    # Объеденение наборов и соответсвенно удаление повторяющихся элементов
# # аналогично строке выше my_nabor3 = my_nabor | my_nabor2
# print(my_nabor3)
#
# my_nabor4 = my_nabor.intersection(my_nabor2)   # Пересечение наборов (вывод повторяющихся элементов)
# # аналогично строке 22 my_nabor4 = my_nabor & my_nabor2
# print(my_nabor4)
#
# my_nabor5 = my_nabor.issubset(my_nabor2)   # Проверка включен ли один набор в другой
# print(my_nabor5)
#
# print(my_nabor2.difference(my_nabor))  # вычитание элементов наборов
# # аналогично строке выше: print(my_nabor2 - my_nabor)
# my_nabor7 = {1, 2, 3}
# print(my_nabor7.discard(2))    # Удаление элемента набора (ещё есть remove)
# print(my_nabor7)
#
# a = {2, 5, 80}
# b = a.copy()
# a.add(70)
# b.add(77)
#
# print(a.symmetric_difference(b))   # Симметричная разница (находит элементы которых нет в пересечение множеств)
# # аналогично верхней строке print((a | b) - (a & b))

"""Задание"""
set_1 = {2, 7, 55, 9, 11}
set_1.add(40)
print(set_1)
set_2 = {2, 7, 4, 8, 3, 40}
set_3 = set_1.intersection(set_2)
print(set_3)
print(list(set_3))
