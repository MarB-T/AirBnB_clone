#!/usr/bin/python3
"""
The module introduces BaseModel of AirBnB project
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel a class that defines all common attributes
    for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        Args:
            *args: Variable length of arguement list.
            **kwargs: Arbitrary keyword arguements.
        """

        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if (key == '__class__'):
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """
        Method that returns a string rep of BaeModel instance.
        """

        print('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.to_dict()))  
        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.to_dict()))

    def save(self):
        """
        Method that saves the current intance.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ 
        Returns dictionary representation of class instance.
        Returns:
            Dict: The dictionary representation
        """

        result = self.__dict__.copy()
        result['__class__'] =  self.__class__.__name__
        result['id'] = self.id
        result['updated_at'] = self.updated_at.isoformat()
        result['created_at'] = self.created_at.isoformat()
        return (result)


if __name__ == '__main__':
    unittest.main()
