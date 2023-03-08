#!/usr/bin/python3
'''contain the state class'''
from os import getenv
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''defines the state class'''
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states', cascade='all, delete-orphan')

    if getenv('HBNB_MYSQL_DB') != 'db':
        @property
        def cities(self):
            '''gets cities linked to state onject'''
            o_l = models.storage.all(City).values()
            return [o for o in o_l if self.id == o.state_id]
