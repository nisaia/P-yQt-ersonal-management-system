from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .book_models import books_metadata, BookStatus
from .movie_models import movies_metadata, MovieStatus

book_engine = create_engine("sqlite:///database/books_database.db", echo=True)
movies_engine = create_engine("sqlite:///database/movies_database.db", echo=True)
#music_engine = create_engine("sqlite:///database/music_database.db", echo=True)

Book_session = sessionmaker(bind=book_engine)
book_session = Book_session()

Movie_session = sessionmaker(bind=movies_engine)
movie_session = Movie_session()

#Music_session = sessionmaker(bind=music_engine)
#music_session = Music_session()

def create_database():
    books_metadata.create_all(book_engine)
    movies_metadata.create_all(movies_engine)

    #SISTEMARE QUESTA COSA# VIOLA IL VINCOLO DI UNICITÀ
    
    for value in ['Not readed', 'In progress', 'Readed']:
        book_status = BookStatus(name=value)
        book_session.add(book_status)
    book_session.commit()

    for value in ['Not watched', 'Watched']:
        movie_status = MovieStatus(name=value)
        movie_session.add(movie_status)
    movie_session.commit()

