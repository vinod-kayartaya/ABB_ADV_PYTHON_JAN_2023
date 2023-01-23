from oop_ex04 import Person

if __name__ == '__main__':

    p1 = Person(name='Vinod', age='49', city=123)
    print(p1)

    # print(dir(p1))
    p1.age = 59
    # p1.__age = 'asdf' # doesn't work
    # p1._Person__age = 'asdf' # works
    # print(dir(p1))
    print(p1)

    p1.name = 'Vinod Kumar'
    print(p1.name)
    print(p1)
