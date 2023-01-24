import threading


def task1():
    for i in range(25):
        print(f'in thread {threading.current_thread().name} i is {i}')


def task2():
    for j in range(25):
        print(f'in thread {threading.current_thread().name} j is {j}')


if __name__ == '__main__':
    t1 = threading.Thread(target=task1, name='task-1')
    t2 = threading.Thread(target=task2, name='task-2')
    print('Created 2 threads')

    t1.start()
    t2.start()

    for k in range(10):
        print(f'in thread {threading.current_thread().name} k is {k}')
