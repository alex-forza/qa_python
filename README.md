# qa_python Sprint_4
1. Проверка на не добавление книги с названием 40+ символов в список книг:
	test_add_new_book_more_negative_sizes

2. Провека на добавление двух книг:
	test_add_new_book_add_two_books_collection_increased

3. Проверка на наличие списка 18+ у созданного объекта:
	test_genre_age_rating_list_is_not_empty

4. Проверка на невозможность добавление двух одинаковых книг:
	test_add_new_book_add_identical_books_add_one_book

5. Проверка задания жанра книги:
	test_set_book_genre_add_genre_book_with_genre

6. Проверка вывода жанра по имени книги:
	test_get_book_genre_add_book_with_genre_get_genre

7. Проверка вывода списка книг по заданному жанру:
	test_get_books_with_specific_genre_empty_list_add_two_books

8. Проверка подходящих детям книг (по жанрам):
	test_get_books_for_children_empty_list_list_increased

9. Проверка отсутствия в списке книг для детей книг с рейтингом 18+:
	test_get_books_for_children_empty_list_only_children_genre

10. Проверка добавления книги в избранное:
	test_add_book_in_favorites_empty_list_list_increased

11. Проверка удаления книги (одной) из списка:
	test_delete_book_from_favorites_add_two_book_list_decreased

12. Проверка невозможности получения пустого списка:
	test_get_books_genre_empty_dict
