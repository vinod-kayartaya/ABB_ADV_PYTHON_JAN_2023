class Person:

    def __init__(self):
        """
        This method is automatically called by the python interpreter when an object is constructed.
        An  object is constructed by treating the name of the class as a function.

        For example,
        Person()

        This is not a call to the __init__(self) method, but it is an instruction to python to create an
        object. After creating the object, python passes the reference to the newly constructed object
        as a parameter to the __init__ method.

        The same reference is also the return value of the constructor call. i.e, Person()

        For example,
        p1 = Person()
        
        p1 has the same value as the self in the __init__ when it was called for Person()
        """
        print(f'Person.__init__ called with self, whose id is {id(self)}')


# execute this block only when this module is run directly (not imported)
if __name__ == '__main__':
    # create an object of Person class
    p1 = Person()
    # p1 is a reference to an object of Person class
    # it has a unique id
    print(f'id of p1 is {id(p1)}')
    p2 = Person()
    print(f'id of p2 is {id(p2)}')

