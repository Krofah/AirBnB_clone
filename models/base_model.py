#!/usr/bin/python3
"""aseModel that defines all common attributes/methods for other classes"""
from uuid import uuid4
from datetime import datetime
class BaseModel:
    def __str__(self):
        """ returns should print: [<class name>] (<self.id>) <self.__dict__>"""
        return"[{}] ([]) []".format(type(self).__name__.self.id,self.__dict__)
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance
        by using self.__dict__, only instance attributes set will be returned
        a key __class__ must be added to this dictionary with the class name of the object
        """
        dict_ = self.__dict__.copy()
        dict_['created_at'] = self.created_at.isoformat()
        dict_['updated_at'] = self.updated_at.isoformat()
        dict_['__class__'] = self.__class__.__name__
        return dict_



