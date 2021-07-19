from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.authors import Author
from flask_app.models.books import Book
from flask_app.models.favorites import Favorite


@app.route('/')
def index():
    session.clear()
    return redirect('/authors')


@app.route('/authors')
def show_all_authors():
    session.clear()
    authors = Author.get_all_authors()
    return render_template('index.html', authors=authors)


@app.route('/author/create', methods=['POST'])
def create_author():
    Author.create_author(request.form)
    return redirect('/authors')


@app.route('/author/<int:author_id>')
def author_info(author_id):
    data = {
        'id': author_id
    }
    session['author'] = Author.get_all_author_favorite_books_by_author_id(data)
    return redirect('/author')


@app.route('/author')
def view_author_with_favorite_books():
    if 'author' in session:
        all_books = Book.get_all_books()
        results = session['author']
        author_data = {
            'id': results[0]['authors.id'],
            'first_name': results[0]['first_name'],
            'last_name': results[0]['last_name']
        }
        author = Author(author_data)
        books = []
        for item in results:
            if item['id'] != None:
                book_data = {
                    'id': item['id'],
                    'title': item['title'],
                }
                new_book = Book(book_data)
                books.append(new_book)

    return render_template('generic.html', author=author, books=books, all_books=all_books) 


@app.route('/books')
def show_all_books():
    session.clear()
    books = Book.get_all_books()
    return render_template('index.html', books=books)

@app.route('/book/create', methods=['POST'])
def create_book():
    Book.create_book(request.form)
    return redirect('/books')

@app.route('/book')
def view_book_with_authors_that_have_favorited():
    if 'book' in session:
        all_authors = Author.get_all_authors()
        results = session['book']
        book_data = {
            'id': results[0]['id'],
            'title': results[0]['title'],
        }
        book = Book(book_data)
        authors = []
        for item in results:
            if item['id'] != None:
                author_data = {
                    'id': item['authors.id'],
                    'first_name': item['first_name'],
                    'last_name': item['last_name']
                }
                new_author = Author(author_data)
                authors.append(new_author)

    return render_template('generic.html', book=book, authors=authors, all_authors=all_authors)

@app.route('/book/<int:book_id>')
def book_info(book_id):
    data = {
        'id': book_id
    }
    session['book'] = Book.get_all_authors_that_favorited_by_book_id(data)
    return redirect('/book')


@app.route('/favorite/create', methods=['POST'])
def create_author_favorite_book():
    Favorite.create_favorites_relationship(request.form)
    return redirect('/')