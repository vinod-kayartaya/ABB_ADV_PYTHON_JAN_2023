import json
from my_classes import Person


if __name__ == '__main__':
    # p1 = dict(name='Vinod', city='Bangalore', email='vinod@vinod.co', is_married=True)
    p1 = Person('Vinod', 'Bangalore', 'vinod@vinod.co')

    # marshall or serialize
    ser_p1 = json.dumps(p1.__dict__)
    print(ser_p1)

    # unmarshall or deserialize
    p2 = json.loads(ser_p1)
    print(p2)
    print(type(p2))

