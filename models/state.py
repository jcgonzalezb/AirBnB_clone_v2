#!/usr/local/bin/python3.9
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

    @property
    def cities(self):
        """ prpperty getter of city"""
        list_cities = []
        for city in models.storage.all("City").values():
            if city.state_id == self.id:
                list_cities.append(city)
        return list_cities

