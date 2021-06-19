from datetime import datetime
from sqlalchemy import Table, Column
from sqlalchemy import Integer, ForeignKey, String, Unicode, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()
movies_metadata = Base.metadata

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    cover_path = Column(String(255), nullable=False)
    year = Column(Integer(), nullable=False)
    film_director_id = Column(Integer(), ForeignKey('film_directors.id'))
    genre_id = Column(Integer(), ForeignKey('genres.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def repr(self):
        return '%r' % self.title

class Film_director(Base):
    __tablename__ = "film_directors"
    id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def repr(self):
        return '%r' % self.id

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key = True)
    name = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    def repr(self):
        return '%r' % self.name

