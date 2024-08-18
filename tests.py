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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    import unittest

    from main import BooksCollector
    class TestBooksCollector(unittest.TestCase):

        def test_add_new_book_success(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            self.assertIn('Гарри Поттер', collector.get_books_genre())

        def test_add_new_book_max_length(self):
            collector = BooksCollector()
            book_name = 'X' * 40
            collector.add_new_book(book_name)
            self.assertIn(book_name, collector.get_books_genre())

        def test_add_new_book_exceeds_max_length(self):
            collector = BooksCollector()
            book_name = 'X' * 41
            collector.add_new_book(book_name)
            self.assertNotIn(book_name, collector.get_books_genre())

        def test_add_new_book_no_duplicate(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            collector.add_new_book('Гарри Поттер')
            self.assertEqual(len(collector.get_books_genre()), 1)

        def test_set_book_genre_success(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            collector.set_book_genre('Гарри Поттер', 'Фантастика')
            self.assertEqual(collector.get_book_genre('Гарри Поттер'), 'Фантастика')

        def test_set_book_genre_invalid_genre(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            collector.set_book_genre('Гарри Поттер', 'Роман')
            self.assertNotEqual(collector.get_book_genre('Гарри Поттер'), 'Роман')

        def test_get_books_with_specific_genre(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            collector.set_book_genre('Гарри Поттер', 'Фантастика')
            self.assertIn('Гарри Поттер', collector.get_books_with_specific_genre('Фантастика'))

        def test_get_books_for_children_no_age_restriction(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            collector.set_book_genre('Гарри Поттер', 'Фантастика')
            self.assertIn('Гарри Поттер', collector.get_books_for_children())

        def test_get_books_for_children_with_age_restriction(self):
            collector = BooksCollector()
            collector.add_new_book('Стивен Кинг')
            collector.set_book_genre('Стивен Кинг', 'Ужасы')
            self.assertNotIn('Стивен Кинг', collector.get_books_for_children())

        def test_add_book_in_favorites_success(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            collector.add_book_in_favorites('Гарри Поттер')
            self.assertIn('Гарри Поттер', collector.get_list_of_favorites_books())

        def test_add_book_in_favorites_not_in_books(self):
            collector = BooksCollector()
            collector.add_book_in_favorites('Неизвестная книга')
            self.assertNotIn('Неизвестная книга', collector.get_list_of_favorites_books())

        def test_delete_book_from_favorites(self):
            collector = BooksCollector()
            collector.add_new_book('Гарри Поттер')
            collector.add_book_in_favorites('Гарри Поттер')
            collector.delete_book_from_favorites('Гарри Поттер')
            self.assertNotIn('Гарри Поттер', collector.get_list_of_favorites_books())

    if __name__ == '__main__':
        unittest.main()