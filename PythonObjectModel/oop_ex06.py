from oop_ex04 import Person

if __name__ == '__main__':
    p1 = Person()
    p1.name = 'Shyam'
    p1.name += ' Sundar'
    p1.age += 30

    print(p1)
    print(f'After 5 years, {p1.name} will be {p1.age + 5} years!')

    p2 = Person(name='John', age=44, city='Dallas')

    p2 += ' Doe'  # p2.name should become 'John Doe'
    p2 += 500  # p2.age should become 49

    print(p2)

