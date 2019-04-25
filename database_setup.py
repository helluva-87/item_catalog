import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Catalog(Base):
    __tablename__ = 'catalog'
    # Here we define columns for the table catalog
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Item(Base):
    __tablename__ = 'item'
    # Here we define columns for the table item.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    item_name = Column(String(250))
    # street_number = Column(String(250))
    item_description = Column(String(250), nullable=False)
    item_id = Column(Integer, ForeignKey('catalog.id'))
    catalog = relationship(Catalog)

# Create an engine that stores data in the local directory's
# catalog_database.db file.
engine = create_engine('sqlite:///catalog_database.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
