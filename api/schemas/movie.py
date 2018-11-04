from marshmallow import fields
from .base_schema import BaseSchema

class MovieSchema(BaseSchema):

    title = fields.String(required=True, error_messages={
        'required': 'the title is a required field'
    })
    description =  fields.String(required=True)
    url = fields.String(required=True)
    
    def load_object_into_schema(self, input_data, partial = False):
        """Helper function to load python objects into schema"""

        data, errors = self.load(input_data, partial = partial)
        if errors:
            return errors, False
        
        return data, True
