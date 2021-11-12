import json
from database.db import book_session
from database.book_models import *

with open('json/genres.json') as genres_json_file:
    data = json.load(genres_json_file)
  
    genres = data['genres']
    for genre in genres:
        id = genre['id']
        name = genre['name']
        new_genre = Genre(id=id, name=name)
        book_session.add(new_genre)
        print(new_genre.name + " created")
    book_session.commit()

with open('json/authors.json') as authors_json_file:
    data = json.load(authors_json_file)

    authors = data['authors']
    for author in authors:
        id = author['id']
        name = author['name']
        surname = author['surname']
        new_author = Author(id=id, name=name, surname=surname)
        book_session.add(new_author)
        print(new_author.name + " " + new_author.surname + " created")
    book_session.commit()

with open('json/books.json') as books_json_file:
    data = json.load(books_json_file)

    books = data['books']
    for book in books:
        print(book)
        id = book['id']
        title = book['title']
        isbn = book['isbn']
        pages = book['pages']
        year = book['year']
        
        author_name = book['author']['name']
        author_surname = book['author']['surname']
        author = book_session.query(Author).filter_by(name=author_name, surname=author_surname).first()
        author_id = author.id
        
        genre_name = book['genre']
        genre = book_session.query(Genre).filter_by(name=genre_name).first()
        print(genre)
        genre_id = genre.id

        status_name = book['status']
        status = book_session.query(BookStatus).filter_by(name=status_name).first()
        status_id = status.id

        new_book = Book(id=id, title=title, isbn=isbn, pages=pages, year=year, author_id=author_id, genre_id=genre_id, status_id=status_id)
        book_session.add(new_book)
    book_session.commit()
