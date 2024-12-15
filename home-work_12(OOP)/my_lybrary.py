class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_available = True  # книга доступна по умолчанию

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Книга '{self.title}' взята.")
        else:
            print(f"Книга '{self.title}' уже взята.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Книга '{self.title}' возвращена.")
        else:
            print(f"Книга '{self.title}' уже доступна.")

    def __str__(self):
        status = "доступна" if self.is_available else "взята"
        return f"'{self.title}' ({self.author}, {self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Книга '{book.title}' удалена из библиотеки.")
                return
        print("Книга с таким ISBN не найдена.")

    def find_books_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        if found_books:
            print(f"Книги автора '{author}':")
            for book in found_books:
                print(book)
        else:
            print(f"Книги автора '{author}' не найдены.")

    def list_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            print("Доступные книги:")
            for book in available_books:
                print(book)
        else:
            print("Нет доступных книг.")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.borrow()
                return
        print("Книга с таким ISBN не найдена.")

    def return_book(self, isbn):
        book_to_return = next((book for book in self.books if book.isbn == isbn), None)
        if book_to_return:
            book_to_return.return_book()
        else:
            print(f"Книга с ISBN {isbn} не найдена.")


def show_menu():
    print("\nМеню:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книги по автору")
    print("4. Показать доступные книги")
    print("5. Взять книгу")
    print("6. Вернуть книгу")
    print("7. Выход")


def main():
    library = Library()

    # Добавим несколько книг в библиотеку
    library.add_book(Book("Преступление и наказание", "Фёдор Достоевский", 1866, "9780451524935"))
    library.add_book(Book("Война и мир", "Лев Толстой", 1869, "9780140447934"))
    library.add_book(Book("Анна Каренина", "Лев Толстой", 1873, "9780140447936"))
    library.add_book(Book("Мёртвые души", "Николай Гоголь", 1842, "978-5-17-094367-7"))

    while True:
        show_menu()
        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            isbn = input("Введите ISBN книги: ")
            library.add_book(Book(title, author, year, isbn))

        elif choice == "2":
            isbn = input("Введите ISBN книги для удаления: ")
            library.remove_book(isbn)

        elif choice == "3":
            author = input("Введите имя автора: ")
            library.find_books_by_author(author)

        elif choice == "4":
            library.list_available_books()

        elif choice == "5":
            isbn = input("Введите ISBN книги для взятия: ")
            library.borrow_book(isbn)

        elif choice == "6":
            isbn = input("Введите ISBN книги для возврата: ")
            library.return_book(isbn)

        elif choice == "7":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
