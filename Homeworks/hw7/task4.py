from time import sleep


def pause(n):
    def decorator(func):
        def wrap(*args, **kwargs):
            print(f"sleep {n} sec")

            sleep(n)

            print(f"{func.__name__} start")

            func(*args, **kwargs)

            print(f"{func.__name__} finish")

            print(f"sleep {n} sec")

            sleep(n)
        return wrap
    return decorator


@pause(3)
def func(a):
    j = 0
    for i in range(a):
        j += 1


func(123)
