class Person:

    def __init__(self):
        # print(f'id of self in __init__ is {id(self)}')
        # we can use the 'self' to store/create member data/variables that are specific
        # to this particular object
        # print(dir(self))
        self.name = 'vinod'
        # print(dir(self))
        self.age = 49
        # print(dir(self))
        self.city = 'bangalore'
        # print(dir(self))

    def print_info(self):
        # print(f'id of self in print_info is {id(self)}')
        print('Information about Person:')
        print(f'Name = {self.name}')
        print(f'Age  = {self.age} years')
        print(f'City = {self.city}')
        print('-'*50)


if __name__ == '__main__':

    p1 = Person()
    p1.print_info()
    # p1 (invoking object) is passed as the first argument (self) to the print_info function

    p2 = Person()
    p2.print_info()
