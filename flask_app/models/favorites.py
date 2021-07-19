from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Favorite():

    def __init__(self, data):
        self.id = data['id']
        self.author_id = data['author_id']
        self.book_id = data['book_id']

    # create a new author
    @classmethod
    def create_favorites_relationship(cls, data):
        query = "INSERT INTO authors_favorite_books (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"

        new_favorites_id = connectToMySQL('booksdb').query_db(query, data)

        return new_favorites_id

    @classmethod
    def delete_favorites_relationship(cls, data):

        query = "DELETE FROM authors_favorite_books WHERE id = %(id)s;"

        connectToMySQL('booksdb').query_db(query, data)