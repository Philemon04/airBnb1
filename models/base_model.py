#!/usr/bin/python3
from _datetime import datetime
import uuid

from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = uuid
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    if key != '__class__':
                        self.__dict__[key] = value
        else:
            storage.new(self)

    def __str__(self):
        classname = self.__class__.__name__
        print('[{}] ({}) {}'.format(classname, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = datetime.strftime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
        new_dict['updated_at'] = datetime.strftime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
