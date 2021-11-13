import json
from database.db import book_session
from database.book_models import *

with open('json/books.json') as books_json_file:
    data = json.load(books_json_file)

    books = data['books']
    for book in books:
        title = book['title']
        isbn = book['isbn']
        pages = book['pages']
        year = book['year']
        description = book['description']
        
        author_name = book['author']['name']
        author_surname = book['author']['surname']
        author = book_session.query(Author).filter_by(name=author_name, surname=author_surname).first()
        if not author:
            author = Author(name=author_name, surname=author_surname)
            book_session.add(author)
            book_session.commit()

        genre_name = book['genre']
        genre = book_session.query(Genre).filter_by(name=genre_name).first()
        if not genre:
            genre = Genre(name=genre_name)
            book_session.add(genre)
            book_session.commit()


        status_name = book['status']
        status = book_session.query(BookStatus).filter_by(name=status_name).first()
        
        new_book = Book(title=title, isbn=isbn, pages=pages, year=year, description=description, author_id=author.id, genre_id=genre.id, status_id=status.id)
        book_session.add(new_book)
    book_session.commit()
