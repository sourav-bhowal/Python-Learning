#### BASIC DECORATOR ####
# def debug(func):
#     def wrapper():
#         return func() 
#     return wrapper


# def hello():
#     print("Hello")

######################################################################################

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{key} = {value}" for key, value in kwargs.items())
        print(f"Calling: {func.__name__} with args: {args_value} and kwargs: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("Hello")

@debug
def greet(name, greeting = "Hello"):
    print(f"{name}, {greeting}")


hello()
greet("Sourav", greeting="jii")