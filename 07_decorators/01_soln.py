import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time")
        return result
    return wrapper

@timer  # when we write the decorator like this "@timer" now the "ex_fn" function will not run directly instead it will pass through the "timer fn "first
def ex_fn(n):
    time.sleep(n)

ex_fn(2)