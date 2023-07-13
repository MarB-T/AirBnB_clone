#!/usr/bin/python3
"""
This module introduces a new clas called FileStorage
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file.
    Deserializes JSON  file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all stored objects.
        """

        return self.__objects

    def new(self, obj):
        """
        Sets the given object with key id.
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes objects to the JSON file specified.
        """

        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserializes the JSON file to objects if it exists
        or it does nothing.
        """

        try:
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                from models.base_model import BaseModel  # Import BaseModel here
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split(".")
                    class_ = eval(class_name)
                    obj = class_(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

