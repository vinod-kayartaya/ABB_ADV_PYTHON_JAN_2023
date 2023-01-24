import pickle

if __name__ == '__main__':
    with open('people.data', 'rb') as f:
        people = pickle.load(f)
        for p in people:
            p.print_info()
