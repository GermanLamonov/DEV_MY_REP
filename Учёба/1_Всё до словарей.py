import emoji
#
# ia = 'German'
# print(ia.lower().count('g'))
#
# x = 5_0
# y = 4.6
# z = int(y)
# print(pow(x, z)) #Возведение в степень
# print(round(y)) #Округление числа
#
# c = '12.6'
# s = float(c)
# print(s)
#
# """Комплексные числа"""
# complex_a = 5 + 3j
# complex_b = 7 + 8j
#
# sum1 = complex_a + complex_b
# print(sum1)
# print(type(sum1))
#
# print(bool(10))
# print(bool('abc'))
# print(bool([]))
# print(bool([1, 2, 3]))
# print(bool(None))
# print('Long string' > 'long') # False потому что сравнение идёт по символам, а 1 символ long c маленькой буквы
int_num = 5
float_num = 4.5
print(float_num + int_num)
"""        Равносильно
print(int_num.__add__(float_num))
# NotImplemented
print(float_num.__radd__(int_num))
    Вызываются магические методы (сами) для выражения разных типов
"""
print("___________________________________________________")
bool_val = True
int_val = 7
print(int_val + bool_val)
print("___________________________________________________")
