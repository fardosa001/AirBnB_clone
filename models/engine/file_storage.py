#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class
    private class attributes:
        __file_path(str):path to the JSON file
        __objects(dict):empty but will store all objects by <class name>.id

    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        info = {}
        for k, obj in self.__objects.items():
            info[k] = obj.to_dict()

        json_string = json.dumps(info)
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json_string)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for info in data.values():
                obj = info["__class__"]
                self.new(eval("{}({})".format(obj, "**info")))
        except FileNotFoundError:
            pass
