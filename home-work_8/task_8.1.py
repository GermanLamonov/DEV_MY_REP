"""
Реализовать программу для подсчёта индекса массы
тела человека. Пользователь вводит рост и вес с клавиатуры.
На выходе – ИМТ и пояснение к нему в зависимости от
попадания в тот или иной диапазон. Использовать обработку
исключений.
"""


def calculate_bmi(weight, height):
    """Функция для расчёта индекса массы тела (ИМТ)."""
    return weight / (height ** 2)


def get_bmi_category(bmi):
    """Функция для определения категории ИМТ."""
    if bmi < 16:
        return "Тяжёлое недоедание"
    elif 16 <= bmi < 16.9:
        return "Недоедание"
    elif 17 <= bmi < 18.4:
        return "Недостаточная масса тела"
    elif 18.5 <= bmi < 24.9:
        return "Нормальная масса тела"
    elif 25 <= bmi < 29.9:
        return "Избыточная масса тела"
    elif 30 <= bmi < 34.9:
        return "Ожирение I степени"
    elif 35 <= bmi < 39.9:
        return "Ожирение II степени"
    else:
        return "Ожирение III степени"


def main():
    try:
        weight = float(input("Введите ваш вес (кг): "))
        height = float(input("Введите ваш рост (м): "))

        if weight <= 0 or height <= 0:
            raise ValueError("Вес и рост должны быть положительными числами.")

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        print(f"Ваш ИМТ: {bmi:.2f}")
        print(f"Категория: {category}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


main()
