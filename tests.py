import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize('book', ['', 'У этой великолепной и несуществующей книги очень длинное название'])
    def test_add_new_book_more_negative_sizes(self, collector, book):
        assert not collector.add_new_book(book)

    def test_add_new_book_add_two_books_collection_increased(self,collector):
        collector.add_new_book('Бегущий по лабиринту')
        collector.add_new_book('Шерлок Холмс')
        assert len(collector.get_books_genre()) == 2

    def test_genre_age_rating_list_is_not_empty(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_add_identical_books_add_one_book(self,collector):
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Шерлок Холмс')
        assert len(collector.get_books_genre()) != 2

    def test_set_book_genre_add_genre_book_with_genre(self,collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно','Ужасы')
        assert {'Оно':'Ужасы'} == collector.get_books_genre()


    def test_get_book_genre_add_book_with_genre_get_genre(self,collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_books_with_specific_genre_empty_list_add_two_books(self,collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Кошмары на улице Вязов')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Кошмары на улице Вязов', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы')==['Оно','Кошмары на улице Вязов']


    def test_get_books_for_children_empty_list_list_increased(self,collector):
        collector.add_new_book('Тачки')
        collector.add_new_book('Бегущий по лабиринту')
        collector.add_new_book('Кот Саймона')
        collector.set_book_genre('Тачки', 'Мультфильмы')
        collector.set_book_genre('Бегущий по лабиринту', 'Фантастика')
        collector.set_book_genre('Кот Саймона', 'Комедии')
        assert len(collector.get_books_for_children()) == 3

    @pytest.mark.parametrize("books_for_adults", ['Ужасы','Детективы'])
    def test_get_books_for_children_empty_list_only_children_genre(self,collector,books_for_adults):
        collector.add_new_book('Оно')
        collector.add_new_book('Тачки')
        collector.add_new_book('Бегущий по лабиринту')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Кот Саймона')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Тачки', 'Мультфильмы')
        collector.set_book_genre('Бегущий по лабиринту', 'Фантастика')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Кот Саймона', 'Комедии')
        for name in collector.get_books_for_children():
            assert name not in collector.get_books_with_specific_genre(books_for_adults)


    def test_add_book_in_favorites_empty_list_list_increased(self,collector):
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.add_book_in_favorites('Шерлок Холмс')
        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс']

    def test_delete_book_from_favorites_add_two_book_list_decreased(self,collector):
        collector.add_new_book('Тачки')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Тачки', 'Мультфильмы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_book_in_favorites('Тачки')
        collector.delete_book_from_favorites('Шерлок Холмс')
        assert collector.get_list_of_favorites_books() ==['Тачки']

    def test_get_books_genre_empty_dict(self, collector):
        assert not collector.get_books_genre()
