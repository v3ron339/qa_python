from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг> всё таи Трёх
    def test_add_new_book_add_three_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Горы и зомби')
        collector.add_new_book('Что делать, если ваш кот очень милый')
        collector.add_new_book('Развод часть Три')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2 у нас будет 3
        assert len(collector.get_books_rating()) == 3

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # Здесь я проверю что Книги Жанра Ужасы и Детективы не попадают в Раздел Детские
class TestBooksCollector:    
         
    def test_book_with_age_rating_not_in_children_list(self):
     collector = BooksCollector()
     collector.add_new_book('Семейка Адемс')
     collector.set_book_genre('Семейка Адемс', 'Ужасы') 

     collector.add_new_book('Шерлок Холмс')
     collector.set_book_genre('Шерлок Холмс', 'Детективы')
           
     children_books = collector.get_books_for_children()
            
     assert 'Семейка Адемс' not in children_books
     assert 'Шерлок Холмс' not in children_books
# Здесб я проверю книгу на отсутствие жанра
class TestBooksCollector:
     
     def test_new_book_has_no_genre_by_default(self):
      collector = BooksCollector()

      collector.add_new_book('Книга без жанра')

      assert collector.get_book_genre('Книга без жанра') == ''
# Жанр можно присвоить, только если он есть в списке доступных
class TestBooksCollector: 
    
     def test_set_book_genre_valid_genre_fantastika(self):
      collector = BooksCollector()
      collector.add_new_book('Гарри Поттер')
      collector.set_book_genre('Гарри Поттер', 'Фантастика')
      assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'


     def test_set_book_genre_valid_genre_komedii(self):
        collector = BooksCollector()
        collector.add_new_book('Частушки')
        collector.set_book_genre('Частушки', 'Комедии')
        assert collector.get_book_genre('Частушки') == 'Комедии'
#  Возвращение книги без возрастного рейтинга для детей 
class TestBooksCollector:   
    
     def test_get_books_for_children_returns_only_safe_books(self):
        collector = BooksCollector()

        collector.add_new_book('Маша и медведь')
        collector.set_book_genre('Маша и медведь', 'Мультфильмы')

        collector.add_new_book('Проклятье')
        collector.set_book_genre('Проклятье', 'Ужасы')

        children_books = collector.get_books_for_children()

        assert 'Маша и медведь' in children_books
        assert 'Фильм ужасов' not in children_books
        #  Присваеваем значение несуществующей книги = None, если книги нет
class TestBooksCollector:      
      
        def test_get_book_genre_returns_none_if_book_not_exists(self):
          collector = BooksCollector()

          assert collector.get_book_genre('Честная книга') is None
          #  Метод get_books_with_specific_genre возвращает список книг заданного жанра
class TestBooksCollector:
        def test_get_books_with_specific_genre_returns_books(self):
         collector = BooksCollector()

         collector.add_new_book('Властелин колец')
         collector.set_book_genre('Властелин колец', 'Фантастика')

         collector.add_new_book('Мстители')
         collector.set_book_genre('Мстители', 'Фантастика')
 
         result = collector.get_books_with_specific_genre('Фантастика')

         assert 'Властелин колец' in result
         assert 'Мстители' in result
         assert len(result) == 2
         # Метод add_book_in_favorites добавляет книгу в избранное
class TestBooksCollector:
    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()

        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')

        assert 'Любимая книга' in collector.get_list_of_favorites_books()

         # Метод delete_book_from_favorites удаляет книгу из избранного
class TestBooksCollector:     
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()

        collector.add_new_book('Книга для удаления')
        collector.add_book_in_favorites('Книга для удаления')

        collector.delete_book_from_favorites('Книга для удаления')

        assert 'Книга для удаления' not in collector.get_list_of_favorites_books()

         # Метод get_list_of_favorites_books возвращает список избранных книг
class TestBooksCollector:      
    def test_get_list_of_favorites_books_returns_list(self):
        collector = BooksCollector()

        collector.add_new_book('Фаворит 1')
        collector.add_new_book('Фаворит 2')

        collector.add_book_in_favorites('Фаворит 1')
        collector.add_book_in_favorites('Фаворит 2')

        favorites = collector.get_list_of_favorites_books()

        assert isinstance(favorites, list)
        assert 'Фаворит 1' in favorites
        assert 'Фаворит 2' in favorites

        assert len(favorites) == 2

# Метод get_book_genre возвращает None если книги нет 
class TestBooksCollector:
    def test_get_book_genre_returns_none_if_book_not_exists(self):
        collector = BooksCollector()
           
        assert collector.get_book_genre('Несуществующая книга') is None 
        # Метод get_books_with_specific_genre возвращает список книг заданного жанра
class TestBooksCollector:
    def test_get_books_with_specific_genre_returns_books(self):
        collector = BooksCollector()

        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')

        collector.add_new_book('Мстители')
        collector.set_book_genre('Мстители', 'Фантастика')

        result = collector.get_books_with_specific_genre('Фантастика')

        assert 'Властелин колец' in result
        assert 'Мстители' in result
        assert len(result) == 2
