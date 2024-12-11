"""
Реализовать программу с функционалом калькулятора
для операций над двумя числами. Числа и операция вводятся
пользователем с клавиатуры. Использовать обработку
исключений.
"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Ошибка: деление на ноль нельзя.")
    return x / y


def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        print("Выберите операцию: ")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")

        operation = input("Введите номер операции (1/2/3/4): ")

        if operation == '1':
            result = add(num1, num2)
        elif operation == '2':
            result = subtract(num1, num2)
        elif operation == '3':
            result = multiply(num1, num2)
        elif operation == '4':
            result = divide(num1, num2)
        else:
            raise ValueError("Неверный ввод операции.")

        print(f"Результат: {result:.2f}")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


calculator()
