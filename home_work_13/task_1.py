# Генератор чисел Фибоначчи
def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


n = int(input("Введите номер числа Фибоначчи: "))
if n <= 0:
    print("Номер должен быть положительным числом.")
else:
    print("Последовательность чисел Фибоначчи:")
    for num in fibonacci_generator(n):
        print(num, end=" ")
