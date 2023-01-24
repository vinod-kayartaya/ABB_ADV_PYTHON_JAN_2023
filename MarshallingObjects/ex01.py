import pickle
from my_classes import Person


if __name__ == '__main__':
    p1 = Person('Vinod', 'Bangalore', 'vinod@vinod.co')

    # marshall or serialize
    ser_p1 = pickle.dumps(p1)
    print(ser_p1)

    # unmarshall or deserialize
    p2 = pickle.loads(ser_p1)
    print(p2)
    print(type(p2))
    p2.print_info()

