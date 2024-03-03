import time

def cache(func):
    cache_value = {}
    # print(cache_value)
    def wrapper(*args):
        if args in cache_value: # if the args in present in cache then print it from there
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result  # if the args are not present in cache then save it in cache
        return result
    return wrapper



@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(4, 5))
