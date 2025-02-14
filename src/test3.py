import time
from functools import wraps

def decorator_1(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        execution_time = et - st
        print(f"{func.__name__} call executed in {execution_time:.4f} sec")
        return result
    return wrapper
