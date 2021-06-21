from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .book_models import books_metadata
from .movie_models import movies_metadata

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