from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))


def create_poetry_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Poem(DeclarativeBase):
    __tablename__ = "poem"

    title = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)
    poem = Column(Text(), nullable=False)
    author = Column(String(250), nullable=False)
    url = Column(String(350), nullable=False)
