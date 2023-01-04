from user import User
from user_serializer import UserSchema
from marshmallow import ValidationError

# Duas formas de fazer:
# Crie o objeto
#user = User('Edi', 'female', 'edi@qa.io', 'active')
# Ou peça para o usuário enviar informações

input_user_data = {}

input_user_data['name'] = input('What is your name? ')
input_user_data['age'] = input('What is your age?')
input_user_data['email'] = input('What is your email?')
input_user_data['active'] = input('Are you here?')

user_schema = UserSchema()
user_dict = user_schema.dumps(input_user_data)

print(user_dict)

# Para realizar validações lançando exceptions

try:
    user_schema = UserSchema()
    user_dict = user_schema.load(input_user_data)
    result = user_schema.dump(user_dict)
    print(result)
except ValidationError as err:
    print(err)
    print(err.valid_data)