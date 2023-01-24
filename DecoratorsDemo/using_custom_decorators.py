from custom_decorators import timer, repeat, timerf


@timer
def factorial(num):
    if not isinstance(num, int):
        raise ValueError(f'input must be an int, but received {type(int)}')

    if num <= 1:
        return 1

    fact = 1
    while num > 1:
        fact *= num
        num -= 1

    return fact


@timerf(time_unit='m')
def fibo(limit):
    a, b = -1, 1
    nums = []
    while limit > 0:
        c = a + b
        nums.append(c)
        a, b = b, c
        limit -= 1
    return nums


@repeat(times=10)
def greeting(username):
    print(f'Hello {username}, How are you doing today?')


if __name__ == '__main__':
    n = 10
    f = factorial(num=n)
    print(f'factorial of {n} is {f}')
    fibo_nums = fibo(10)
    print(f'first 10 Fibonacii numbers {fibo_nums}')

    greeting(username='Vinod')
