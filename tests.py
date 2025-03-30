import pytest


class TestBooksCollector:
    # Тест 1: добавление книги (позитивный сценарий)
    @pytest.mark.parametrize("book_name", ["Ведьмак", "Мастер и Маргарита", "Алиса в Стране чудес"])
    def test_add_new_book_positive(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    # Тест 2: добавление книги с пустым именем или слишком длинным именем (негативный сценарий)
    @pytest.mark.parametrize("book_name", ["", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiu."])
    def test_add_new_book_invalid_name_negative(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    # Тест 3: установка жанра книге (позитивный сценарий)
    @pytest.mark.parametrize("book_name, genre", [
        ("Ведьмак", "Фэнтези"),
        ("Мастер и Маргарита", "Классика"),
    ])
    def test_set_book_genre_positive(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тест 4: установка недопустимого жанра (негативный сценарий)
    def test_set_invalid_book_genre_negative(self, collector):
        collector.add_new_book("Ведьмак")
        collector.set_book_genre("Ведьмак", "Роман")  # Жанра нет в списке
        assert collector.get_book_genre("Ведьмак") == ""

    # Тест 5: получение книг определённого жанра (позитивный сценарий)
    def test_get_books_with_specific_genre_positive(self, collector):
        collector.add_new_book("Ведьмак")
        collector.set_book_genre("Ведьмак", "Фэнтези")
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Классика")

        assert collector.get_books_with_specific_genre("Фэнтези") == ["Ведьмак"]
        assert collector.get_books_with_specific_genre("Классика") == ["Мастер и Маргарита"]

    # Тест 6: книга для детей включена в список (позитивный сценарий)
    def test_get_books_for_children_included_positive(self, collector):
        collector.add_new_book("Алиса в Стране чудес")
        collector.set_book_genre("Алиса в Стране чудес", "Приключения")

        children_books = collector.get_books_for_children()
        assert "Алиса в Стране чудес" in children_books

    # Тест 7: книга с возрастным ограничением исключена из списка (негативный сценарий)
    def test_get_books_for_children_excluded_negative(self, collector):
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")  # Ужасы - возрастное ограничение

        children_books = collector.get_books_for_children()
        assert "Оно" not in children_books

    # Тест 8: добавление книги в избранное (позитивный сценарий)
    def test_add_book_in_favorites_positive(self, collector):
        collector.add_new_book("Ведьмак")
        collector.add_book_in_favorites("Ведьмак")
        assert "Ведьмак" in collector.get_list_of_favorites_books()

    # Тест 9: удаление книги из избранного (позитивный сценарий)
    def test_delete_book_from_favorites_positive(self, collector):
        collector.add_new_book("Ведьмак")
        collector.add_book_in_favorites("Ведьмак")
        collector.delete_book_from_favorites("Ведьмак")
        assert "Ведьмак" not in collector.get_list_of_favorites_books()

    # Тест 10: получение списка избранных книг (позитивный сценарий)
    def test_get_list_of_favorites_books_positive(self, collector):
        collector.add_new_book("Ведьмак")
        collector.add_new_book("Мастер и Маргарита")
        collector.add_book_in_favorites("Ведьмак")

        favorites = collector.get_list_of_favorites_books()
        assert favorites == ["Ведьмак"]

    # Тест 11: получение словаря books_genre (позитивный сценарий)
    def test_get_books_genre_positive(self, collector):
        collector.add_new_book("Ведьмак")
        collector.set_book_genre("Ведьмак", "Фэнтези")
        assert collector.get_books_genre() == {"Ведьмак": "Фэнтези"}

    # Тест 12: получение жанра книги (позитивный сценарий)
    def test_get_book_genre_positive(self, collector):
        collector.add_new_book("Ведьмак")
        collector.set_book_genre("Ведьмак", "Фэнтези")
        assert collector.get_book_genre("Ведьмак") == "Фэнтези"