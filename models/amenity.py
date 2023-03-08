#!/usr/bin/python
'''contains the amanity class'''

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''defines the Amenity class'''
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    places_amenitites = relationship('Place', secondary='place_amenity')
