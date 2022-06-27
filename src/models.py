import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table users
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)
    log = relationship('Log', backref='users', lazy=True)


class List(Base):
    __tablename__ = 'lists'
    # Here we define columns for the table lists
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))


class Log(Base):
    __tablename__ = 'logs'
    # Here we define columns for the table logs.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    checker = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

    list_id = Column(Integer, ForeignKey('lists.id'))
    list = relationship(List)


class Character(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table characters
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    planetOfBirth = Column(String(50), nullable=False)
    mainSkill = Column(String(50), nullable=False)
    militancy = Column(String(50), nullable=False)

    planet = relationship('Planet', back_populates='character', uselist=False)


class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table planets
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    spaceQuadrant = Column(String(250), nullable=False)
    kindOfSurface = Column(String(50), nullable=False)

    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Character', back_populates="planet")

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
