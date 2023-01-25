class Person:

    def __init__(self, name, city='Bangalore', age=22):
        self.name = name
        self.age = age
        self.city = city

    def print_info(self):
        print('Information about Person:')
        print(f'Name = {self.name}')
        print(f'Age  = {self.age} years')
        print(f'City = {self.city}')
        print('-' * 50)


if __name__ == '__main__':
    p1 = Person('Vinod', 'Bangalore', 49)
    p1.print_info()

    p2 = Person('John Doe', 'Dallas', 45)
    p2.print_info()

    p3 = Person('Jane Doe', 'Washington')
    p3.print_info()

    p4 = Person('Umesh')
    p4.print_info()

    p5 = Person(age=50, name='Rahul')
    p5.print_info()

    p6 = Person(city='Mumbai', name='Rajesh', age=18)
    p6.print_info()
