USE booksdb;

-- Query: Create 5 different authors: Jane Austen, Emily Dickinson, Fyodor Dostoevsky, William Shakespeare, Lau Tzu
-- INSERT INTO authors (first_name, last_name) 
-- VALUES('Jane', 'Austen');

-- INSERT INTO authors (first_name, last_name) 
-- VALUES('Emily', 'Dickinson');

-- INSERT INTO authors (first_name, last_name) 
-- VALUES('Fyodor', 'Dostoevsky');

-- INSERT INTO authors (first_name, last_name) 
-- VALUES('William', 'Shakespeare');

-- INSERT INTO authors (first_name, last_name) 
-- VALUES('Lau', 'Tzu');

-- Query: Retrieve all the users
SELECT *
FROM authors;

-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
-- INSERT INTO books (title) 
-- VALUES('C Sharp');

-- INSERT INTO books (title) 
-- VALUES('Java');

-- INSERT INTO books (title) 
-- VALUES('Python');

-- INSERT INTO books (title) 
-- VALUES('PHP');

-- INSERT INTO books (title) 
-- VALUES('Ruby');

-- Query: Retrieve all the users
SELECT *
FROM books;

-- Query: Change the name of the C Sharp book to C#
-- UPDATE books 
-- SET title = 'C#'
-- WHERE title = 'C Sharp';

-- Query: Retrieve all the users
SELECT *
FROM books;

-- Query: Change the first name of the 4th author to Bill
-- UPDATE authors 
-- SET first_name = 'Bill'
-- WHERE id = 4;

-- Query: Retrieve all the users
SELECT *
FROM authors;

-- Query: Have the first author favorite the first 2 books
-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(1, 1);

-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(1, 2);

-- Query: Retrieve all the users
SELECT *
FROM authors_favorite_books;

-- Query: Have the second author favorite the first 3 books
-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(2, 1);

-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(2, 2);

-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(2, 3);

-- Query: Retrieve all the users
SELECT *
FROM authors_favorite_books;

-- Query: Have the third author favorite the first 4 books
-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(3, 1);

-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(3, 2);

-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(3, 3);

-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(3, 4);

-- Query: Retrieve all the users
SELECT *
FROM authors_favorite_books;

-- Query: Have the fourth author favorite all the books
-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(4, 1);

-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(4, 2);

-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(4, 3);

-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(4, 4);

-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(4, 5);

-- Query: Retrieve all the users
SELECT *
FROM authors_favorite_books;

-- Query: Retrieve all the authors who favorited the 3rd book
SELECT authors.first_name, authors.last_name
FROM authors
JOIN authors_favorite_books ON authors.id = authors_favorite_books.author_id
WHERE authors_favorite_books.book_id = 3;

-- Query: Remove the first author of the 3rd book's favorites
-- DELETE FROM authors 
-- WHERE authors.id = (
-- SELECT authors.id
-- FROM authors
-- JOIN authors_favorite_books ON authors.id = authors_favorite_books.author_id
-- WHERE authors_favorite_books.book_id = 3 AND authors.id = 2);

-- Query: Retrieve all the users
SELECT *
FROM authors;

-- Query: Add the 5th author as an other who favorited the 2nd book
-- INSERT INTO authors_favorite_books (author_id, book_id) 
-- VALUES(5, 2);

-- Query: Retrieve all the users
SELECT *
FROM authors_favorite_books;

-- Find all the books that the 3rd author favorited
SELECT books.title AS third_author_faves
FROM books
JOIN authors_favorite_books ON books.id = authors_favorite_books.book_id 
JOIN authors ON authors_favorite_books.author_id = authors.id
WHERE authorS.id = 3;

-- Query: Find all the authors that favorited to the 5th book
SELECT authors.first_name
FROM authors
JOIN authors_favorite_books ON authors.id = authors_favorite_books.author_id
JOIN books ON authors_favorite_books.book_id = books.id
WHERE books.id = 5;











