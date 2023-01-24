import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Executed {func.__name__} function in {(end-start)*1000} ms')
        return result

    return wrapper


def timerf(time_unit):
    def timer_decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            execution_time = end - start
            if time_unit == 'ms':
                print(f'Executed {func.__name__} function in {execution_time*1000:.25f} milliseconds')
            elif time_unit == 's':
                print(f'Executed {func.__name__} function in {execution_time:.25f} seconds')
            elif time_unit == 'm':
                print(f'Executed {func.__name__} function in {execution_time/60:.25f} minutes')
            return result

        return wrapper
    return timer_decorator


def repeat(times):
    def repeat_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return repeat_decorator
