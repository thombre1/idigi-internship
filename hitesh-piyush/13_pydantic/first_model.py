from pydantic import BaseModel

# zod like thingy that checks data type
class User(BaseModel):
    id: int
    name: str
    is_active: bool = True

input_data = {
    'id': 21,
    'name': "Aditya",
    'is_active': True
}

# Everything is a string, pydantic will recover it and not show warnings 
dumb_input_data = {
    'id': "21",
    'name': "Aditya",
    'is_active': 'True'
}


user1 = User(**input_data)
user2 = User(**dumb_input_data)

print(user1)
print(user2)

print(type(user1))
