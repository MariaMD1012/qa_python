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

    class TestBooksCollector:
        def test_add_book(books_collector):
            books_collector.add_new_book(NAME)
            assert books_collector.favorites == []
            assert books_collector.books_rating == {NAME: 1}




def books_collector():
    return BooksCollector()

    NAME = 'Book Name'
    WRONG_NAME = 'Wrong Name'


    class TestBooksCollector:
        def test_add_rating_to_absent_book_fails(books_collector):
             books_collector.add_new_book(NAME)
             books_collector.set_book_rating(WRONG_NAME, 5)
             assert books_collector.favorites == []
             assert books_collector.books_rating == {NAME: 1}

    class TestBooksCollector:
        def test_cant_set_rating_less_than_one(books_collector):
            books_collector.add_new_book(NAME)
            books_collector.set_book_rating(NAME, 0)
            assert books_collector.favorites == []
            assert books_collector.books_rating == {NAME: 1}

    class TestBooksCollector:
        def test_cant_set_rating_greater_than_ten(books_collector):
            books_collector.add_new_book(NAME)
            books_collector.set_book_rating(NAME, 11)
            assert books_collector.favorites == []
            assert books_collector.books_rating == {NAME: 1}

    class TestBooksCollector:
        def test_absent_book_has_no_rating(books_collector):
            books_collector.add_new_book(NAME)
            rating = books_collector.get_book_rating(WRONG_NAME)
            assert rating is None

    class TestBooksCollector:
        def test_add_to_favorites(books_collector):
            books_collector.add_new_book(NAME)
            books_collector.add_book_in_favorites(NAME)
            assert books_collector.favorites == [NAME]
            assert books_collector.books_rating == {NAME: 1}

    class TestBooksCollector:
        def test_add_to_favorites_fails_if_not_in_ratings(books_collector):
            books_collector.add_book_in_favorites(NAME)
            assert books_collector.favorites == []
            assert books_collector.books_rating == {}

    class TestBooksCollector:
        def test_delete_from_favorites(books_collector):
            books_collector.add_new_book(NAME)
            books_collector.add_book_in_favorites(NAME)
            books_collector.delete_book_from_favorites(NAME)
            assert books_collector.favorites == []
            assert books_collector.books_rating == {NAME: 1}

    class TestBooksCollector:
        def test_get_list_of_favorites_books(books_collector):
            books_collector.add_new_book(NAME)
            books_collector.add_book_in_favorites(NAME)
            assert books_collector.get_list_of_favorites_books() == [NAME]

    class TestBooksCollector:
        def test_get_books_with_specific_rating_fails_if_wrong_rating(books_collector):
            books_collector.add_new_book(NAME)
            result = books_collector.get_books_with_specific_rating(0)
            assert [] == result