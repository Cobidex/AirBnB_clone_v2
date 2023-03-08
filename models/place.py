#!/usr/bin/python3
'''contains the place class'''
from os import getenv
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from sqlalchemy import *

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_ids', String(60),
                             ForeignKey('amenities.id'),
                      primary_key=True, nullable=False))


class Place(BaseModel, Base):
    '''defines the Place class'''
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship('Review', backref='place',
                           cascade='all, delete-orphan')
    amenities = relationship('Amenity', secondary='place_amenity',
                             viewonly=False)
    if getenv('HBNB_TYPE_STORAGE=db') != 'db':
        @property
        def reviews(self):
            '''
                getter method for place/review
                relationship in filestorage
            '''
            rev = models.storage.all(Review).values()
            return [o for o in rev if self.id == o.place_id]

        @property
        def amenities(self):
            '''getter method for place/amenity'''
            am = models.storage.all(Amenity).values()
            return [o for o in am if self.id in o.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            '''appends id to amenities_ids'''
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
                obj.save()
