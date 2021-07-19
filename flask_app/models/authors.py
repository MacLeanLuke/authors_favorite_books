from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Author():

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.favorite_books = []

    # create a new author
    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"

        new_author_id = connectToMySQL('booksdb').query_db(query, data)

        return new_author_id

    @classmethod
    def delete_author(cls, data):

        query = "DELETE FROM authors WHERE id = %(id)s;"

        connectToMySQL('booksdb').query_db(query, data)

    @classmethod
    def update_author(cls, data):

        # UPDATE table_name SET column_name1 = 'some_value', column_name2='another_value' WHERE condition(s)

        query = "UPDATE authors SET first_name = %(first_name)s, first_name = %(first_name)s WHERE id = %(id)s;"

        connectToMySQL('booksdb').query_db(query, data)

    # return all authors
    @classmethod
    def get_all_authors(cls):

        query = "SELECT * FROM authors;"

        results = connectToMySQL('booksdb').query_db(query)

        # return results

        authors = []

        for item in results:
            new_author = Author(item)
            authors.append(new_author)

        return authors

    @classmethod
    def get_all_author_favorite_books_by_author_id(cls, data):

        query = "SELECT * FROM books JOIN authors_favorite_books ON books.id = authors_favorite_books.book_id JOIN authors ON authors_favorite_books.author_id = authors.id WHERE authors.id = %(id)s;" 

        results = connectToMySQL('booksdb').query_db(query, data)

        print(results)

        return results
