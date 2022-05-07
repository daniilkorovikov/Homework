# Implement a decorator call_once which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.

def call_once(foo):

    cash = None

    def wrapper(*args, **kwargs):
        nonlocal cash
        if cash is None:
            cash = foo(*args, **kwargs)
        return cash

    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
# 55
print(sum_of_numbers(999, 100))
# 55
print(sum_of_numbers(134, 412))
# 55
print(sum_of_numbers(856, 232))
# 55