# """Магические методы в классах"""
#
#
# class Comment2:
#     def __init__(self, text):
#         self.text = text
#         self.votes_qty = 0
#
#     def upvote(self):
#         self.votes_qty += 1
#
#     def __add__(self, other):
#         return [f"{self.text} {other.text}",
#                 self.votes_qty + other.votes_qty]    # Вернули словарь (можно хоть кортеж , словарь)
#
#     def __eq__(self, other):
#         # Сравниваем тексты напрямую
#         return self.text == other.text
#
#     def __lt__(self, other):
#         # Сравниваем тексты по алфавиту (меньше, чем)
#         return self.text < other.text
#
#
# first_comment2 = Comment2("First comment")
# first_comment2.upvote()
# second_comment2 = Comment2("Second text")
# second_comment2.upvote()
# print(first_comment2 + second_comment2)
# print(first_comment2 == second_comment2)   # не выдаёт ошибку без метода __eq__ ,
# # потому что python  использует стандартную
# # реализацию которая сравнивает идентичность объектов в памяти (они по факту разные)
# # False т.к. тексты разные
# print(first_comment2 < second_comment2)    # True, так как "First comment" < "Second comment"

"""Наследование из других классов"""

"""Метод __init__ родительского клааса вызовется автоматически"""


# class RebenokList(list):
#     def func_list(self):
#         print(f"Список имеет {len(self)} элемента")
#
#
# custom_list = RebenokList([2, 5, 7, 8])
# custom_list.func_list()
# custom_list.append(3)
# custom_list.func_list()

"""Пример наследования классов ещё один"""


# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#
# class AdminUser(User):
#     def __init__(self, username, email, role):
#         super().__init__(username, email)    # для родщительского конструктора
#         self.role = role
#         self.is_admin = True
#
#
# my_admin = AdminUser('admin123', 'admin@admin.com', 'Administrator')
# print(my_admin)
# print(type(my_admin))
# print(my_admin.__dict__)
# my_user = User('German123', 'german@german.com')
# print(my_user.__dict__)
# print(User.__subclasses__())

"""Пример:"""
"""Создадим Форум, на форуме пользователи смогут создавать посты, и создадим для этого 3 класса"""


class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author


class Forum:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, username: str, email: str):   # Создаем пользователей
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title: str, content: str, author: User):   # Создаем посты
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def find_user_by_username(self, username: str):    # Поиск пользователя по имени
        for user in self.users:
            if user.username == username:
                return user

    def find_user_by_email(self, email: str):   # Поиск пользователя по мылу
        for user in self.users:
            if user.email == email:
                return user

    def find_posts_by_author(self, author: User):    # Находим пост конкретного пользователя
        found_posts = []
        for post in self.posts:
            if post.author == author:
                found_posts.append(post)
        return found_posts


forum = Forum()

german = forum.register_user('german123', 'german@gmail.com')
artem = forum.register_user('artem228', 'artem@loh.com')
print(forum.users)

forum.create_post('Ky', 'Zdarova zaebal', german)
forum.create_post('Шо?', 'Ебало офф', german)
forum.create_post('Poka', 'Poka zaebal', artem)
print(forum.posts)

"""Не следует таких искать посты по индексу"""
# print(forum.posts[0].title)
# print(forum.posts[0].content)
# print(forum.posts[0].author.username)
# print(forum.posts[0].author.email)

print(forum.find_user_by_username('german12'))   # None
print(forum.find_user_by_username('german123').email)   # german@gmail.com

"""Поиск постов юзера"""
found_posts = forum.find_posts_by_author(german)   # Поиск по имени автора
print(found_posts)
found_posts_titles = [post.title for post in found_posts]    # Здесь выдаем заголовок найденного пользователя
print(found_posts_titles)

"""Поиск юзера по мылу и поиск всех постов этого юзера и нету при этом фактического объекта юзера"""
user_email = 'german@gmail.com'
found_user = forum.find_user_by_email(user_email)
if found_user:
    print(forum.find_posts_by_author(found_user))
else:
    print(f"Юзер с таким мылом {user_email} не найден ")





