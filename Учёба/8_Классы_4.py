"""Инкапсуляция — это принцип объектно-ориентированного программирования, который заключается в ограничении доступа к
внутренним данным объекта и предоставлении методов для безопасного взаимодействия с ними.
Это позволяет скрывать детали реализации и защищать данные от некорректного использования.
В Python инкапсуляция достигается с помощью:

Приватных атрибутов (с помощью одного или двух подчеркиваний перед именем атрибута).
Геттеров и сеттеров — методов для получения и изменения значений приватных атрибутов."""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Приватный атрибут

    # Геттер для получения баланса
    def get_balance(self):
        return self.__balance

    # Сеттер для изменения баланса
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    # Метод для снятия денег
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")


# Создаем экземпляр класса BankAccount
account = BankAccount("John", 1000)

# Используем методы для работы с балансом
print(account.get_balance())  # Output: 1000

account.deposit(500)
print(account.get_balance())  # Output: 1500

account.withdraw(200)
print(account.get_balance())  # Output: 1300

"""Декоратор @property в Python превращает метод в свойство (property), которое можно использовать как атрибут, 
то есть без явного вызова метода (без скобок). Это позволяет вам упростить доступ к значениям, а также добавляет 
дополнительный контроль над тем, как эти значения вычисляются или изменяются.

Когда вы используете @property, Python автоматически вызывает соответствующий метод, 
но синтаксически это выглядит как доступ к атрибуту объекта, а не как вызов метода.

Геттер (getter): Метод, помеченный как @property, становится геттером для атрибута. Это значит, что вы можете обращаться
 к нему как к атрибуту, но фактически Python будет вызывать метод, который выполнит вычисления или обработку данных.

Сеттер (setter): Если вы хотите изменять значение, то используете декоратор @property для создания геттера и 
@<property_name>.setter для сеттера. Сеттер позволяет контролировать процесс присваивания значения атрибуту.

Удобство: Вместо того, чтобы каждый раз вызывать метод с круглыми скобками (например, rect.get_area()), вы можете 
обращаться к методу как к атрибуту, например rect.area
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width  # Приватный атрибут
        self._height = height  # Приватный атрибут

    @property
    def area(self):
        # Геттер для свойства area
        return self._width * self._height

    @property
    def width(self):
        return self._width  # Геттер для атрибута width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width must be positive")

    @property
    def height(self):
        return self._height  # Геттер для атрибута height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Height must be positive")


# Создаем экземпляр класса Rectangle
rect = Rectangle(10, 5)

# Используем свойство для получения площади
print(rect.area)  # Output: 50

# Изменяем ширину через сеттер
rect.width = 15

# Площадь пересчитывается с новым значением ширины
print(rect.area)  # Output: 75
