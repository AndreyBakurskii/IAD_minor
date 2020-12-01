def save_args2file(path2file: str):
    def decorator(func):
        def wrap(*args, **kwargs):
            with open(path2file, "a") as file:
                file.write(f"{func.__name__}: args - {args}, kwargs - {kwargs}\n")

            func(*args, **kwargs)
        return wrap
    return decorator


@save_args2file("logging.txt")
def func1(*args, **kwargs):
    pass


@save_args2file("logging.txt")
def func2(*args, **kwargs):
    pass


func1(1, 2, 3, 4, a=2, b=3, c=5)
func2(0, 9, 8, 7, l=12, k=32, j=76)
