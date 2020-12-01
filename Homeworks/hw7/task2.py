def log_outputs(func_outputs: dict):
    def decorator(func):
        def wrap(*args, **kwargs):
            key = f"args - {args}, kwargs - {kwargs}"

            if key in func_outputs:
                return func_outputs[key]
            else:
                func_outputs[key] = func(*args, **kwargs)
                return func_outputs[key]

        return wrap
    return decorator


fib_outputs = dict()


@log_outputs(fib_outputs)
def fib(a: int):
    if a == 0:
        return 0

    if a == 1:
        return 1

    return fib(a - 1) + fib(a - 2)


print(fib(40))
