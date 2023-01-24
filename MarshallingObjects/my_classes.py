class Person:
    def __init__(self, name, city, email):
        self.name = name
        self.city = city
        self.email = email

    def print_info(self):
        print(f'Name    : {self.name}')
        print(f'City    : {self.city}')
        print(f'Email   : {self.email}')
        print()

    def __str__(self):
        return f'Person(name="{self.name}", city="{self.city}", email="{self.email}")'

