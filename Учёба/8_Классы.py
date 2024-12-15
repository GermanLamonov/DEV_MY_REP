"""
self - это объект который вызывает метод (my_car = self в примере)

class Car:
    def move(self):
    print("Car go")

my_car = Car()
my_car.move()
"""

"""Задание"""


# class Image:
#
#     def __init__(self, resolution, title, extension):
#         self.resolution = resolution
#         self.title = title
#         self.extension = extension
#
#     def __str__(self):
#         return f"Название {self.title}, Разрешение {self.resolution}, Формат {self.extension}"
#
#     def resize(self, new_resolution):
#         self.resolution = new_resolution
#         print(f'Разрешение изменилось на {self.resolution}')
#
#     def retitle(self, new_title):
#         self.title = new_title
#         print(f'Название изменилось на {self.title}')
#
#
# image_1 = Image('800x600', 'German', 'jpg')
# image_2 = Image('640x480', 'Nebesniy', 'png')
# print(f"Разрешение 1 картинки: {image_1.resolution}")
# image_1.resize('1280x960')
# print("Картинка 1:", image_1)
# print()
# print(f"Разрешение 2 картинки: {image_2.resolution}")
# image_2.resize('800x600')
# print(f"Название картинки 2: {image_2.title}")
# image_2.retitle('Francyz')
# print("Картинка 2:", image_2)

"""Статические методы доступны как атрибуты класса
        и как атрибуты экземпляров класса
"""


# class Comment:
#
#     def __init__(self, text):
#         self.text = text
#
#     @staticmethod
#     def merge_comments(first, second):
#         return f"{first} {second}"
#
#
# my_comment = Comment("My comment")
# m_1 = Comment.merge_comments("Thanks!", "Excellent")   # как атрибут класса
# print(m_1)
# m_2 = my_comment.merge_comments("Great", "OK")   # как атрибут экземпляра класса
# print(m_2)


"""Атрибуты класса
   К ним можно обращатся от экземляров,
   но изменять их можно только обращением от класса!
"""


class Comment1:
    total_comments = 0

    def __init__(self, text):
        self.text = text
        Comment1.total_comments += 1    # при создание экземлпяра класса(коментария) число комментариев будет
        # увеличиватся используя атрибут класса


first_comment = Comment1("First comment")
print("Количество комментариев:", Comment1.total_comments)
second_comment = Comment1("Second comment")
print("Количество комментариев:", Comment1.total_comments)
