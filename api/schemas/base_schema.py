from abc import ABC
from marshmallow import Schema


class BaseSchema(Schema):
    def load_object_into_schema(self, input_data, partial = False):
        """Helper function to load python objects into schema"""

        data, errors = self.load(input_data, partial = partial)
        if errors:
            return errors, False
        
        return data, True
        