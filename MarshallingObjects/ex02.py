import pickle
from my_classes import Person


if __name__ == '__main__':
    people = [
        Person('Vinod', 'Bangalore', 'vinod@vinod.co'),
        Person('Shyam', 'Mysore', 'shyam@xmpl.com'),
        Person('Harish', 'Mangalore', 'harish@xmpl.com')
    ]

    with open('people.data', 'wb') as f:
        pickle.dump(people, f)
        print('Data saved in file people.data')
