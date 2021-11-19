import json
from database.db import book_session, movie_session
from database import book_models
from database import movie_models

with open('json/data.json') as data_json_file:
    data = json.load(data_json_file)

    books = data['books']
    for book in books:
        title = book['title']
        isbn = book['isbn']
        pages = book['pages']
        year = book['year']
        description = book['description']
        
        author_name = book['author']['name']
        author_surname = book['author']['surname']
        author = book_session.query(book_models.Author).filter_by(name=author_name, surname=author_surname).first()
        if not author:
            author = book_models.Author(name=author_name, surname=author_surname)
            book_session.add(author)
            book_session.commit()

        genre_name = book['genre']
        genre = book_session.query(book_models.Genre).filter_by(name=genre_name).first()
        if not genre:
            genre = book_models.Genre(name=genre_name)
            book_session.add(genre)
            book_session.commit()


        status_name = book['status']
        status = book_session.query(book_models.BookStatus).filter_by(name=status_name).first()
        
        new_book = book_models.Book(title=title, isbn=isbn, pages=pages, year=year, description=description, author_id=author.id, genre_id=genre.id, status_id=status.id)
        book_session.add(new_book)
    book_session.commit()

    movies = data['movies']
    for movie in movies:
        title = movie['title']
        film_length = movie['film_length']
        year = movie['year']
        description = movie['description']

        film_director_name = movie['film_director']['name']
        film_director_surname = movie['film_director']['surname']
        film_director = movie_session.query(movie_models.Film_director).filter_by(name=film_director_name, surname=film_director_surname).first()
        if not film_director:
            film_director = movie_models.Film_director(name=film_director_name, surname=film_director_surname)
            movie_session.add(film_director)
            movie_session.commit()
        
        genre_name = movie['genre']
        genre = movie_session.query(movie_models.Genre).filter_by(name=genre_name).first()
        if not genre:
            genre = movie_models.Genre(name=genre_name)
            movie_session.add(genre)
            movie_session.commit()
        
        status_name = movie['status']
        status = movie_session.query(movie_models.MovieStatus).filter_by(name=status_name).first()

        new_movie = movie_models.Movie(title=title, film_length=film_length, year=year, description=description, film_director_id = film_director.id, genre_id=genre.id, status_id=status.id)
        movie_session.add(new_movie)
    movie_session.commit()
