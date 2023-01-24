import json
from my_classes import Person


if __name__ == '__main__':
    people = [
        Person('Vinod', 'Bangalore', 'vinod@vinod.co'),
        Person('Shyam', 'Mysore', 'shyam@xmpl.com'),
        Person('Harish', 'Mangalore', 'harish@xmpl.com')
    ]

    with open('people.json', 'wt') as f:
        json.dump([p.__dict__ for p in people], f)
        print('Data saved in file people.json')
