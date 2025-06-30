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

books_collector = BooksCollector()

# инициализации объекта перед каждым тестом

@pytest.fixture
def collector(self):
    return BooksCollector()
    
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

# проверка добавления одной и той же книги 

def test_add_duplicate_book(self, collector):
    collector.add_new_book('Дубровский')
    collector.add_new_book('Дубровский')
    assert len(collector.books_genre) == 1