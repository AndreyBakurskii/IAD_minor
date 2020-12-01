import time


def work_time(func):
    def wrap(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"{func.__name__} working {time.time() - start}")
    return wrap


@work_time
def func(a):
    j = 0
    for i in range(a):
        j += 1


func(1234890)
