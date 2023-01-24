import json

if __name__ == '__main__':
    with open('people.json', 'rt') as f:
        people = json.load(f)
        for p in people:
            print(p)
