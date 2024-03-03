# def square_number(number):
#     print("Square of", number, "is:", number**2)


# number = int(input("Enter a number: "))
# square_number(number)

################################ OR #################################
def square_number(number):
    return number**2


number = int(input("Enter a number: "))
result = square_number(number)
print("Square of", number, "is:", result)