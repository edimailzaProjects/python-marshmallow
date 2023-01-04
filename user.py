class User:
    def __init__(self, name, age, email, active):
        self.name = name
        self.age = age
        self.email = email
        self.active = active

    def __repr__(self):
        return f'{self.name} is {self.age} years old, and the e-amil is: {self.email}. Is the user active? {self.active}'
