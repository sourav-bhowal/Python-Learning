def factorial(number):
    if number == 0:
        return 1
    else:
       return number*factorial(number-1) 

print(factorial(5))

################################ OR #################################
def factorial(number):
    if number >= 1:
        return number*factorial(number-1)
    else:
        return 1


print(factorial(5))