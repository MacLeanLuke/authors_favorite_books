from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Book():

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']

    # create a new author
    @classmethod
    def create_book(cls, data):
        query = "INSERT INTO books (title) VALUES (%(title)s);"

        new_book_id = connectToMySQL('booksdb').query_db(query, data)

        return new_book_id

    @classmethod
    def delete_book(cls, data):

        query = "DELETE FROM books WHERE id = %(id)s;"

        connectToMySQL('booksdb').query_db(query, data)

    @classmethod
    def update_book(cls, data):

        # UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)

        query = "UPDATE books SET title = %(title)s WHERE id = %(id)s;"

        connectToMySQL('booksdb').query_db(query, data)

    # return all authors
    @classmethod
    def get_all_books(cls):

        query = "SELECT * FROM books;"

        results = connectToMySQL('booksdb').query_db(query)

        # return results

        books = []

        for item in results:
            new_book = Book(item)
            books.append(new_book)

        return books

    @classmethod
    def get_all_authors_that_favorited_by_book_id(cls, data):

        query = "SELECT * FROM books JOIN authors_favorite_books ON books.id = authors_favorite_books.book_id JOIN authors ON authors_favorite_books.author_id = authors.id WHERE books.id = %(id)s;" 

        results = connectToMySQL('booksdb').query_db(query, data)

        print(results)

        return results