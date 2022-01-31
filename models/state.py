#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """ Return list of city instances if
            City.state_id==current State.id.
            FileStorage relationship between State and City"""
            from models import storage
            from models.city import City
            list_cities = []
            for k, obj_city in storage.all(City).values():
                if obj_city.state_id == self.id:
                    list_cities.append(obj_city)
            return list_cities
