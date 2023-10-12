from _datetime import datetime
import uuid


class BaseModel:
    id = uuid
    created_at = datetime.today()
    updated_at = datetime.today()

    def __str__(self):
        classname = self.__class__.__name__
        print('[{}] ({}) {}'.format(classname, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        return new_dict
