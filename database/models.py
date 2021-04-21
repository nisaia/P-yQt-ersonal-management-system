from datetime import datetime
from sqlalchemy import Table, Column
from sqlalchemy import Integer, ForeignKey, String, Unicode, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()
metadata = Base.metadata

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    isbn = Column(String(255), unique=True, nullable=False)
    description = Column(String(255))
    cover_path = Column(String(255), nullable=False)
    category_id = Column(Integer(), ForeignKey('categories.id'))
    author_id = Column(Integer(), ForeignKey('authors.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def repr(self):
        return '%r' % self.title

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key = True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def repr(self):
        return '%r' % self.id

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key = True)
    name = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    def repr(self):
        return '%r' % self.name
