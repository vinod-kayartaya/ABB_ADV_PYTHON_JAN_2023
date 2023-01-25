class Person:

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.age = kwargs.get('age', 20)
        self.city = kwargs.get('city', 'Bangalore')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value is None or type(value) == str:
            self.__name = value
        else:
            raise ValueError('value must be a <str>')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('age must be an <int>')
        if value < 1 or value > 120:
            raise ValueError('age must be between 1 and 120 years')
        self.__age = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise ValueError('city must be an <str>')
        self.__city = value

    def print_info(self):
        print('Information about Person:')
        print(f'Name = {self.__name}')
        print(f'Age  = {self.__age} years')
        print(f'City = {self.__city}')
        print('-' * 50)

    def __iadd__(self, value):
        if isinstance(value, str):
            self.name += value
        elif isinstance(value, int):
            self.age += value
        else:
            raise ValueError(f'{type(value)}  is incompatible type with += on Person type')
        return self

    def __str__(self):
        return f'Person(name="{self.__name}", age={self.__age}, city="{self.__city}")'


if __name__ == '__main__':

    p4 = Person(name='Ramesh')
    p4.print_info()

    p5 = Person(age='asd', name='Rahul')
    p5.print_info()

    p6 = Person(city='Mumbai', name='Rajesh', age=18)
    p6.print_info()
