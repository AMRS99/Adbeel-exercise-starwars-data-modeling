import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String,unique=False, nullable=False)
    last_name = Column(String,unique=False, nullable=False)
    email = Column(String,unique=True, nullable=False)
    password =Column(Integer,unique=False, nullable=False)
    subscription_date = Column(String,unique=False, nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True) 
    birth_year = Column(String, unique= False,nullable=False) 
    eye_color = Column(String, unique= False,nullable=False)
    gender = Column(String, unique= False,nullable=False)
    hair_color = Column(String, unique= False,nullable=False)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String, unique= False,nullable=False)
    diameter = Column(Integer, unique= False,nullable=False)
    gravity = Column(Integer, unique= False,nullable=False)
    name = Column(String, unique= False,nullable=False)
    orbital_period = Column(Integer, unique= False,nullable=False)
    population = Column(Integer, unique= False,nullable=False)
    rotation_period = Column(Integer, unique= False,nullable=False)
    surface_water = Column(Integer, unique= False,nullable=False)
    terrain = Column(String, unique= False,nullable=False)
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(Integer, unique= False,nullable=False)
    consumables = Column(String, unique= False,nullable=False)
    crew = Column(Integer, unique= False,nullable=False)
    length = Column(Integer, unique= False,nullable=False)
    manufacturer = Column(String, unique= False,nullable=False)
    model = Column(String, unique= False,nullable=False)
    name = Column(String, unique= False,nullable=False)
    passengers = Column(Integer, unique= False,nullable=False)

class Favorite(Base):
    __tablename__='favorites'
    id = Column (Integer, primary_key=True)
    vehicle_id = Column(Integer,ForeignKey('vehicles.id'))
    vehicle = relationship(Vehicle)
    planet_id = Column(Integer,ForeignKey('planets.id'))
    planet = relationship(Planet)
    character_id = Column(Integer,ForeignKey('characters.id'))
    character = relationship(Character)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
