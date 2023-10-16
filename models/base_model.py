#!/usr/bin/python3
"""class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class
    Attributes:
        id(str): assign with an uuid when an instance is created
        created_at(datetime): assign with the current datetime.
        updated_at(datetime): updated every time you change your object

    """
    def __init__(self, *args, **kwargs):
        """Initializes Attributes
        Args:
            args(tuple): arguments
            kwargs(dict): keyword arguments
        """
        if kwargs:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.isoformat(val))
                elif key != '__class__':
                    setattr(self, key, val)

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        models.storage.new(self)

    def __str__(self):
        """string representation of the class"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the public instance attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        class_dict = self.__dict__.copy()
        class_dict['__class__'] = self.__class__.__name__
        class_dict['created_at'] = self.created_at.isoformat()
        class_dict['updated_at'] = self.updated_at.isoformat()

        return class_dict
