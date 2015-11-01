from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import date
from datetime import datetime
import os

path = os.environ['MYPATH']
ENGINE = create_engine(path, echo=True)

sqla_session = scoped_session(sessionmaker(bind=ENGINE, autocommit=False, autoflush=False))
Base = declarative_base()
Base.query = sqla_session.query_property()


class Hit(Base):

	__tablename__ = "hits"

	id = Column(Integer, primary_key=True)
	hit_date = Column(DateTime(timezone=False), nullable=True)


def create_db():
	"""Recreates the db."""
	Base.metadata.create_all(ENGINE)