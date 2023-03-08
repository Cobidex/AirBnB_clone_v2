#!/usr/bin/python3
'''modele for user definitions'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    '''defines the User Class'''
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', backref='user',
                          cascade='all, delete-orphan')
    reviews = relationship('Review', backref='user',
                           cascade='all, delete-orphan')
