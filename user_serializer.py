from marshmallow import Schema, fields, post_load, ValidationError, validates, validate
from user import User

class UserSchema(Schema):
        name = fields.Str()
        age = fields.Integer()
        email = fields.Email()
        active = fields.Boolean()
    
        @validates('age')
        def validate_age(self,age):
                if age > 150:
                        raise ValidationError('The age is too old!')

        @post_load
        def create_user(self, data, **kwargs):
                return User(**data)
