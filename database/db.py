from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import metadata

engine = create_engine("sqlite:///database/database.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def create_database():
    metadata.create_all(engine)