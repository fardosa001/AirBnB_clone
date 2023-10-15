#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """FileStorage class
    private class attributes:
        __file_path(str):path to the JSON file
        __objects(dict):empty but will store all objects by <class name>.id

    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User}
    @classmethod
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    @classmethod
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[k] = obj

    @classmethod
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        info = {}
        for k, obj in self.__objects.items():
            info[k] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(info, f)

    @classmethod
    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                info = json.load(f)
            for k, val in info.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[k] = obj
        except Exception:
            pass
