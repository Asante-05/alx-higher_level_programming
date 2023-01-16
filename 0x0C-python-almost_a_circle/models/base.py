#!/usr/bin/python3
""" base module """


import json


class Base:
    """  base class
    with private attribute
    """

    __nb_objects = 0

    """class constructor
    """
    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method
        Args:
            list_dictionaries(list): a list of dictionaries
        Returns: the json representation of the list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ class function
        Args:
            cls(class object): first argument
            list_objs: second argument
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as j_File:
            if list_objs is None:
                j_File.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                j_File.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ static method
        Args:
            json_string(string): represent a list of dicts
        Return:
            list of json string representation
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ class method
        Args:
            dictionary: double pointer to a dictionary
        Return:
            a class instance created from a dictionary of attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ class method
        Returns: list of class intances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as j_File:
                list_dict = Base.from_json_string(j_File.read())
                return [cls.create(**obj) for obj in list_dict]
        except IOError:
            return []
