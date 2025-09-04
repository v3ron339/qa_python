# qa_python
# Проект: Тестирование BooksCollector

В этом проекте реализованы юнит-тесты для класса BooksCollector, написанные с использованием библиотеки pytest.

## Описание

Класс BooksCollector позволяет:
- хранить список книг и жанров,
- задавать жанры для книг,
- определять книги, подходящие детям,
- добавлять книги в избранное и удалять их.

Тестами покрыты основные сценарии работы методов.

## Реализованные тесты

- test_add_new_book_add_three_books — проверка добавления трёх книг в словарь.
- test_added_book_has_no_genre_by_default — у добавленной книги нет жанра по умолчанию.
- test_set_book_genre_valid_genre_fantastika — установка жанра «Фантастика».
- test_set_book_genre_valid_genre_komedii — установка жанра «Комедии».
- test_get_books_for_children_excludes_books_with_age_rating — книги с возрастным ограничением не попадают в список для детей.
- test_get_book_genre_returns_none_if_book_not_exists - Присваивание книги значения None.
- test_get_books_with_specific_genre_returns_books Создает список книг заданого Жанра.
- test_add_book_in_favorites_adds_book_successfully — добавление книги в избранное.
- test_delete_book_from_favorites_removes_book — удаление книги из избранного.
- test_get_list_of_favorites_books_returns_correct_list — получение списка избранных книг.
