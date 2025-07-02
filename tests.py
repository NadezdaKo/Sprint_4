from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


import pytest


# Тесты для add_new_book (валидация)

@pytest.mark.parametrize('name, expected', [
    ('Война и мир', True),
    ('X' * 41, False),  # 41 символ
    ('', False),  # пустая строка
    ('@&^', False)
    ])
def test_add_new_book_validation(self, collector, name, expected):
    collector.add_new_book(name)
    assert (name in collector.books_genre) == expected


books_collector = BooksCollector()

# проверка добавления одной и той же книги 

def test_add_duplicate_book(self, collector):
    collector.add_new_book('Дубровский')
    collector.add_new_book('Дубровский')
    assert len(collector.books_genre) == 1


books_collector = BooksCollector()

# Тесты для set_book_genre (жанр книги)
def test_set_valid_genre_true(self, collector):
    collector.add_new_book('Метро 2033')
    collector.set_book_genre('Метро 2033', 'Фантастика')
    assert collector.get_book_genre('Метро 2033') == 'Фантастика'


books_collector = BooksCollector()

def test_set_invalid_genre_false(self, collector):
    collector.add_new_book('Грозовой перевал')
    collector.set_book_genre('Грозовой перевал', 'Роман')  # недопустимый жанр
    assert collector.get_book_genre('Грозовой перевал') == ''


books_collector = BooksCollector()

# получаем жанр книги по её имени
def test_get_book_genre_add_book(self):

    # Добавляем книгу с жанром
    book_name = 'Пункт назначения'
    genre = 'Ужасы'
    books_collector.add_new_book(book_name)
    books_collector.set_book_genre(book_name, genre)
    received_genre = books_collector.get_book_genre(book_name) # Получаем жанр книги
    
    # Проверяем, что полученный жанр соответствует установленному
    assert received_genre == genre, f"Ожидался жанр {genre}, но получен {received_genre}"


books_collector = BooksCollector()

# Тесты для get_books_with_specific_genre (книги с определенным жанром)
def test_get_books_by_genre(self, collector):
    collector.add_new_book('Аватар')
    collector.add_new_book('Оно')
    collector.set_book_genre('Аватар', 'Фантастика')
    collector.set_book_genre('Оно', 'Ужасы')
    assert collector.get_books_with_specific_genre('Фантастика') == ['Аватар']


books_collector = BooksCollector()

# Тесты для get_books_for_children (подходящие детям)
def test_get_books_for_children(self, collector):
    collector.add_new_book('Шрек')
    collector.add_new_book('Сияние')
    collector.set_book_genre('Шрек', 'Мультфильмы')
    collector.set_book_genre('Сияние', 'Ужасы')
    assert 'Шрек' in collector.get_books_for_children()
    assert 'Сияние' not in collector.get_books_for_children()


books_collector = BooksCollector()

# Тест на добавление книги в избранное
def test_add_book_in_favorites(self):
    book_name = 'Война и мир'

     # Проверяем успешное добавление
    self.books_collector.add_book_in_favorites(book_name)
    assert book_name in self.books_collector.favorites


books_collector = BooksCollector()

# Тест на удаление книги из избранного
def test_delete_book_from_favorites(self):
    book_name = 'Грозовой перевал'
        
    # Добавляем книгу для тестирования удаления
    self.books_collector.add_book_in_favorites(book_name)
        
    # Удаляем книгу и проверяем результат
    self.books_collector.delete_book_from_favorites(book_name)
    assert book_name not in self.books_collector.favorites


books_collector = BooksCollector()

# Тест на получение списка избранных книг
def test_get_list_of_favorites_books(self):
    # Добавляем несколько книг в избранное
    self.books_collector.add_book_in_favorites('Война и мир')
    self.books_collector.add_book_in_favorites('Шрек')
        
    # Получаем список избранных книг
    favorites_list = self.books_collector.get_list_of_favorites_books()
        
    # Проверяем корректность списка
    assert len(favorites_list) == 2
    assert 'Война и мир' in favorites_list
    assert 'Шрек' in favorites_list


books_collector = BooksCollector()

# Тест на работу с пустым списком избранного
def test_empty_favorites_list(self):
    # Проверяем пустой список
    assert self.books_collector.get_list_of_favorites_books() == []