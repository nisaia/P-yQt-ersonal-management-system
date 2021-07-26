from datetime import datetime
from sqlalchemy import Table, Column
from sqlalchemy import Integer, ForeignKey, String, Unicode, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()
books_metadata = Base.metadata

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    isbn = Column(String(255), unique=True, nullable=False)
    pages = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(String(255))
    cover_path = Column(String(255), nullable=False)
    genre_id = Column(Integer(), ForeignKey('genres.id'))
    author_id = Column(Integer(), ForeignKey('authors.id'))
    status_id = Column(Integer(), ForeignKey('status.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def repr(self):
        return '%r' % self.title

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer(), primary_key = True)
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

class Status(Base):
    __tablename__ = "status"
    id = Column(Integer, primary_key = True)
    name = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)