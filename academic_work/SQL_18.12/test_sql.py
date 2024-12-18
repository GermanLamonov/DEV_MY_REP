"""
Создайте базу данных:

Назовите её library.db.
Создайте таблицу books: Таблица должна содержать следующие поля:

id — уникальный идентификатор книги (целое число, PRIMARY KEY, AUTOINCREMENT).
title — название книги (текст).
author — автор книги (текст).
year — год выпуска (целое число).
available — доступность книги (логическое значение: 1 — доступна, 0 — недоступна).
Добавьте данные в таблицу: Вставьте 5 записей в таблицу books, например:


1. "1984", George Orwell, 1949, доступна
2. "To Kill a Mockingbird", Harper Lee, 1960, доступна
3. "The Great Gatsby", F. Scott Fitzgerald, 1925, недоступна
4. "Moby Dick", Herman Melville, 1851, доступна
5. "War and Peace", Leo Tolstoy, 1869, недоступна
Выполните запросы:

Выберите все книги, которые доступны.
Найдите книги, выпущенные после 1950 года.
Обновите доступность книги "The Great Gatsby" на "доступна".
Удалите из таблицы книгу "Moby Dick".
Сохраните изменения: Убедитесь, что данные сохраняются в базе после выполнения запросов.
"""
import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('library.db')
cursor = connection.cursor()

# # Создаем таблицу books
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Books (
# id INTEGER PRIMARY KEY,
# title TEXT NOT NULL,
# author TEXT NOT NULL,
# year INTEGER,
# available BLOB
# )

# ''')
#
# # Добавляем новые книги
# cursor.execute('INSERT INTO books (title, author, year, available) VALUES'
#                "('1984','George Orwell', 1949, 1),"
#                "('To Kill a Mockingbird', 'Harper Lee', 1960, 1),"
#                "('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 0),"
#                "('Moby Dick', 'Herman Melville', 1851, 1),"
#                "('War and Peace', 'Leo Tolstoy', 1869, 0);"
#                )

# Выбираем книги которые доступны
cursor.execute('SELECT title, author FROM Books WHERE available = ?', (1,))
results = cursor.fetchall()

print('Доступные книги:')
for book in results:
  print(book)

connection.commit()

# Находим книги, выпущенные после 1950 года.
cursor.execute('SELECT title, year FROM Books WHERE year > ?', (1950,))
results = cursor.fetchall()

print('\nКниги выпущенные после 1950 года:')
for book in results:
  print(book)

connection.commit()

# Обновляем доступность книги "The Great Gatsby" на "доступна".
cursor.execute('UPDATE Books SET available = ? WHERE title = ?', (1, 'The Great Gatsby'))
connection.commit()

# Удаляем из таблицы книгу "Moby Dick".
cursor.execute('DELETE FROM Books WHERE title = ?', ('Moby Dick',))
connection.commit()

# Выбираем все книги
cursor.execute('SELECT * FROM Books')
books = cursor.fetchall()

# Выводим результаты
for book in books:
  print(book)

# Закрываем соединение
connection.close()

