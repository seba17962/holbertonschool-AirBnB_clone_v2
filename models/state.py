#!/usr/bin/python3
""" State for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel):
    """ State class created."""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @ property
        def cities(self):
            """Return all cities."""
            from models import storage
            my_list = []
            for i in list(storage.all(City).values()):
                if self.id == i.state_id:
                    my_list.append(i)
            return my_list
