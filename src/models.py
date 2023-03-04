import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()  

class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    favorite = relationship('favorite')

class Favorite(Base):
    __tablename__='favorite'
    id = Column(Integer, primary_key=True)
    pokemon_id = Column(Integer, ForeignKey('pokemon'))
    name = Column(String(50), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id'))
    
class Pokemon(Base):
    __tablename__='pokemon'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    ability = relationship('ability')
    attack = relationship('attack')
    

class Feature(Base):
    __tablename__='feature'
    id = Column(Integer, primary_key=True)
    height = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    pokemon = relationship('pokemon')

class Ability(Base):
    __tablename__='ability'
    id = Column(Integer, primary_key=True)
    ability = Column(String(50), nullable=False)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))

class stat(Base):
    __tablename__='stat'
    id = Column(Integer, primary_key=True)
    hp = Column(Integer, nullable=False)
    attack = Column(Integer, nullable=False)
    defense = Column(Integer, nullable=False)
    special_attack = Column(Integer, nullable=False)
    special_defense = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))
    pokemon = relationship('pokemon')

class Type(Base):
    __tablename__='type'
    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    pokemon_id = Column(Integer, ForeignKey('pokemon.id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')