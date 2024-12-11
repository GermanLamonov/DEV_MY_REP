class Car:
    def __init__(self, color, type_car, year):
        self.color = color
        self.type = type_car
        self.year = year

    def __str__(self):
        return f"Цвет: {self.color}, Кузов: {self.type}, Год: {self.year}"

    def start(self):
        print("Автомобиль заведён")

    def disable(self):
        print("Автомобиль заглушен")

    def color_auto(self, color):
        self.color = color
        print(f"Цвет автомобиля изменён на: {color}")
    def type_auto(self, type_car):
        self.type = type_car
        print(f"Тип автомобиля теперь: {type_car}")
    def year_auto(self, year):
        self.year = year
        print(f"Год автомобиля: {year}")


auto = Car('Синий', 'Универсал', 1996)
print(auto)
auto.start()
auto.disable()
auto.color_auto('Красный')
auto.type_auto('Седан')
auto.year_auto(2000)
print(auto)



