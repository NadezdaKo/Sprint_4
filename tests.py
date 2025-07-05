from main import BooksCollector

import pytest

from conftest import books_collector

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
        # assert len(collector.get_books_rating()) == 2
        

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # Тесты для add_new_book (валидация)

    @pytest.mark.parametrize('name, expected', [
        ('Война и мир', True),
        ('X' * 41, False),  # 41 символ
        ('', False)  # пустая строка
        ])
    
    def test_add_new_book_validation(self, books_collector, name, expected):
        books_collector.add_new_book(name)
        assert (name in books_collector.books_genre) == expected


    # проверка добавления одной и той же книги 

    def test_add_duplicate_book(self, books_collector):
        books_collector.add_new_book('Дубровский')
        books_collector.add_new_book('Дубровский')
        assert len(books_collector.books_genre) == 1


    # Тесты для set_book_genre (жанр книги)
    def test_set_valid_genre_true(self, books_collector):
        books_collector.add_new_book('Метро 2033')
        books_collector.set_book_genre('Метро 2033', 'Фантастика')
        assert books_collector.get_book_genre('Метро 2033') == 'Фантастика'


    def test_set_invalid_genre_false(self, books_collector):
        books_collector.add_new_book('Грозовой перевал')
        books_collector.set_book_genre('Грозовой перевал', 'Роман')  # недопустимый жанр
        assert books_collector.get_book_genre('Грозовой перевал') == ''


    # получаем жанр книги по её имени
    def test_get_book_genre_add_book(self, books_collector):

        # Добавляем книгу с жанром
        book_name = 'Пункт назначения'
        genre = 'Ужасы'
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
        received_genre = books_collector.get_book_genre(book_name) # Получаем жанр книги
        
        # Проверяем, что полученный жанр соответствует установленному
        assert received_genre == books_collector.books_genre[book_name], f"Ожидался жанр {genre}, но получен {received_genre}"


    # Тесты для get_books_with_specific_genre (книги с определенным жанром)
    def test_get_books_by_genre(self, books_collector):
        books_collector.add_new_book('Аватар')
        books_collector.add_new_book('Оно')
        books_collector.set_book_genre('Аватар', 'Фантастика')
        books_collector.set_book_genre('Оно', 'Ужасы')
        assert books_collector.get_books_with_specific_genre('Фантастика') == ['Аватар']


    # Проверка метода get_books_genre 

    def test_get_books_genre(self, books_collector):
            # Добавляем книги в словарь
        books_collector.add_new_book('Оно')
        books_collector.set_book_genre('Оно', 'Ужасы')
            
        books_collector.add_new_book('Аватар')
        books_collector.set_book_genre('Аватар', 'Фантастика')
            
            # Получаем словарь жанров
        genres_dict = books_collector.get_books_genre()
            
            # Проверяем корректность результата
        expected_genres = {
                'Оно': 'Ужасы',
                'Аватар': 'Фантастика'
            }
        assert genres_dict == expected_genres


    # Тесты для get_books_for_children (подходящие детям)
    def test_get_books_for_children(self, books_collector):
        books_collector.add_new_book('Шрек')
        books_collector.add_new_book('Сияние')
        books_collector.set_book_genre('Шрек', 'Мультфильмы')
        books_collector.set_book_genre('Сияние', 'Ужасы')
        assert 'Шрек' in books_collector.get_books_for_children()
        assert 'Сияние' not in books_collector.get_books_for_children()


    # Тест на добавление книги в избранное
    def test_add_book_in_favorites(self, books_collector):
        book_name = 'Война и мир'
        books_collector.add_new_book(book_name)  # Добавляем книгу в каталог
        books_collector.set_book_genre(book_name, 'Роман')  # Устанавливаем жанр

        # Проверяем успешное добавление
        books_collector.add_book_in_favorites(book_name)
        assert book_name in books_collector.favorites


    # Тест на удаление книги из избранного
    def test_delete_book_from_favorites(self, books_collector):
        book_name = 'Грозовой перевал'
        books_collector.add_new_book(book_name)  # Добавляем книгу в каталог
        books_collector.set_book_genre(book_name, 'Роман')  # Устанавливаем жанр
            
        # Добавляем книгу для тестирования удаления
        books_collector.add_book_in_favorites(book_name)
            
        # Удаляем книгу и проверяем результат
        books_collector.delete_book_from_favorites(book_name)
        assert book_name not in books_collector.favorites


    # Тест на получение списка избранных книг
    def test_get_list_of_favorites_books(self, books_collector):
        # Добавляем книги в словарь
        books_collector.add_new_book('Война и мир')
        books_collector.set_book_genre('Война и мир', 'Роман')
            
        books_collector.add_new_book('Шрек')
        books_collector.set_book_genre('Шрек', 'Мультфильм')

        # Добавляем несколько книг в избранное
        books_collector.add_book_in_favorites('Война и мир')
        books_collector.add_book_in_favorites('Шрек')
            
        # Получаем список избранных книг
        favorites_list = books_collector.get_list_of_favorites_books()
            
        # Проверяем корректность списка
        assert len(favorites_list) == len(books_collector.favorites)
        assert 'Война и мир' in favorites_list
        assert 'Шрек' in favorites_list


    # Тест на работу с пустым списком избранного
    def test_empty_favorites_list(self, books_collector):
        # Проверяем пустой список
        assert books_collector.get_list_of_favorites_books() == []