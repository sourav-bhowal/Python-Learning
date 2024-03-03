def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i # "yield" not "return" as "return will terminate the function every time"


for num in even_generator(10):
    print(num)        