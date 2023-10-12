#!/usr/bin/python3

import json


class FileStorage(object):
    """Define class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Function to return var __objects

        Returns:
            dict: list of objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """

        :rtype: object
        :type obj: object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """

        :rtype: object
        """
        with open(self.__file_path, "w") as my_file:
            my_file.write(json.dumps(FileStorage.__objects.items()))

    def reload(self):
        """

        :rtype: object
        """
        if self.__file_path is not None:

            new_dict = json.loads(self.__file_path)
            for key, value in new_dict.items():
                FileStorage.__objects[key] = value
