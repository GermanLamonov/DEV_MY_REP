import math


class Sphere:
    def __init__(self, r=1, x=0, y=0, z=0):
        self.radius = r
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    def get_square(self):
        return 4 * math.pi * (self.radius ** 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.x, self.y, self.x

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2 + (z - self.z) ** 2)
        return distance < self.radius


sphere = Sphere(2, 2, 3, 3)

# Получение объема
print(f"Объем сферы: {sphere.get_volume()}")

# Получение площади поверхности
print(f"Площадь поверхности сферы: {sphere.get_square()}")

# Получение радиуса
print(f"Радиус сферы: {sphere.get_radius()}")

# Получение координат центра
print(f"Центр сферы: {sphere.get_center()}")

# Изменение радиуса
sphere.set_radius(5)
print(f"Новый радиус сферы: {sphere.get_radius()}")

# Изменение центра
sphere.set_center(0, 0, 0)
print(f"Новый центр сферы: {sphere.get_center()}")

# Проверка, находится ли точка внутри сферы
point_inside = sphere.is_point_inside(1, 1, 1)
print(f"Точка (1, 1, 1) внутри сферы? {point_inside}")

point_outside = sphere.is_point_inside(10, 10, 10)
print(f"Точка (10, 10, 10) внутри сферы? {point_outside}")