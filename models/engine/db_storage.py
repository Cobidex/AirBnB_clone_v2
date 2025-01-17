#!/usr/bin/python
'''this module contains the db_storage class'''
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class DBStorage():
    '''defines the DBStorage class'''
    __engine = None
    __session = None
               

    def __init__(self):
        c = 'mysql+mysqldb://{}:{}@{}/{}'. format(getenv('HBNB_MYSQL_USER'),
                                                  getenv('HBNB_MYSQL_PWD'),
                                                  getenv('HBNB_MYSQL_HOST'),
                                                  getenv('HBNB_MYSQL_DB'))
        self.__engine = create_engine(c, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''gets objects of specific class'''
        o_d = {}
        if cls:
            query = self.__session.query(eval(cls.__name__)).all()
            for o in query:
                k = "{}.{}". format(o.__class__.__name__, o.id)
                o_d[k] = o
        else:
            for c in [State, City, User, Place, Amenity, Review]:
                query = self.__session.query(c).all()
                for o in query:
                    k = "{}.{}". format(o.__class__.__name__, o.id)
                    o_d[k] = o
        return o_d

    def new(self, obj):
        '''adds the object to current database session'''
        self.__session.add(obj)

    def save(self):
        '''commit changes to current db session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from the current session'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''create all classes'''
        Base.metadata.create_all(self.__engine)
        session_f = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_f)
        self.__session = Session()

    def close(self):
        '''closes the current session'''
        self.__session.close()
