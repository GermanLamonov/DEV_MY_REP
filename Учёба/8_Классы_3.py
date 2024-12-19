"""Абстракция в ООП

Абстрактные методы не имеют реализации в родительском классе,
и они должны быть реализованы в дочерних классах.

Преимущества абстракции:
Сокрытие деталей реализации: Абстракция помогает скрыть сложные детали реализации и предоставляет только важную информацию для пользователя.
Упрощение работы с объектами: Пользователи могут работать с абстракцией (например, с типом Animal), не зная, как конкретно реализованы методы в дочерних классах.
Гибкость: Абстрактные классы позволяют легко добавлять новые типы объектов, следуя единому интерфейсу, без изменения существующего кода.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "Dog runs"


class Cat(Animal):
    def speak(self):
        return "Meow!"

    def move(self):
        return "Cat walks"


# Создаем экземпляры классов
dog = Dog()
cat = Cat()

# Вызываем методы
print("Собака делает", dog.speak())  # Output: Woof!
print(dog.move())  # Output: Dog runs

print("Кот делает", cat.speak())  # Output: Meow!
print(cat.move())  # Output: Cat walks
