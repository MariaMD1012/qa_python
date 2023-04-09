from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Бесы')
        assert collector.books_rating == {'Бесы': 1}

    def test_add_rating_to_absent_book_fails(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Буратино')
        collector.set_book_rating('Буратино', 5)
        assert collector.favorites == []
        assert collector.books_rating == {'Приключения Буратино': 1}

    def test_cant_set_rating_less_than_one(self):
        collector = BooksCollector()
        collector.add_new_book('Унесенные ветром')
        collector.set_book_rating('Унесенные ветром', 0)
        assert collector.books_rating == {'Унесенные ветром': 1}

    def test_cant_set_rating_greater_than_ten(self):
        collector = BooksCollector()
        collector.add_new_book('Дюны')
        collector.set_book_rating('Дюны', 11)
        assert collector.favorites == []
        assert collector.books_rating == {'Дюны': 1}

    def test_absent_book_has_no_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Алиса в стране чудес')
        rating = collector.get_book_rating('Двадцать лет спустя')
        assert rating is None

    def test_add_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Королева Марго')
        collector.favorites == ['Королева Марго']
        assert collector.books_rating == {'Мастер и Маргарита': 1}

    def test_add_to_favorites_fails_if_not_in_ratings(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Гранатовый браслет')
        assert collector.favorites == []
        assert collector.books_rating == {}

    def test_delete_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Вишневый сад')
        collector.add_book_in_favorites('Евгений Онегин')
        collector.delete_book_from_favorites('Идиот')
        assert collector.favorites == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Братья Карамазовы')
        collector.add_book_in_favorites('Война и мир')
        collector.get_list_of_favorites_books() == ['Братья Карамазовы']

    def test_get_books_with_specific_rating_fails_if_wrong_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Мёртвые души')
        result = collector.get_books_with_specific_rating(0)
        assert [] == result