#!/usr/bin/python3
""" Module Base """
import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ representation JSON of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Write the JSON representation of list_objs"""
        fn = "{}.json".format(cls.__name__)

        with open(fn, 'w') as f:
            new_list = []
            if list_objs is None:
                f.write(new_list)
            else:
                for i in list_objs:
                    new_list.append(i.to_dictionary())
                f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ Returns list of the JSON string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return instance with all attr setted """
        if cls.__name__ == "Square":
            dummy = cls(2)
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ List of instances """
        new_list = []
        fn = "{}.json".format(cls.__name__)
        try:
            with open(fn, 'r') as f:
                new_list = cls.from_json_string(f.read())
            for i, j in enumerate(new_list):
                new_list[i] = cls.create(**new[i])
        except Exception:
            pass
        return new_list
