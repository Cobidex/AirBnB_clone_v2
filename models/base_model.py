#!/usr/bin/python
'''
    this module contains the base model for all classes of this project
'''
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel():
    '''the model to be inherited by all other classes'''

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'updated_at' or key == 'created_at':
                    val = datetime.strptime(value,\
                                                     '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, val)
                else:
                    setattr(self, key, value)
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = self.created_at
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        '''returns string representation of object'''
        cls = self.__class__.__name__
        return '[{}] ({}) {}'. format(cls, self.id, self.__dict__)

    def save(self):
        '''updates instance attribute update_at with current datetime'''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''returns dictionary form of object'''
        my_dict = self.__dict__.copy()
        if '_sa_instance_state' in my_dict:
            del my_dict['_sa_instance_state']
        cls = self.__class__.__name__
        my_dict['__class__'] = cls
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return (my_dict)


    def delete():
        '''deletes the current instance'''
        models.storage.delete(self)
