num = 3
fact = 1

while (num > 0 and fact > 0):
    fact = fact*num
    num = num - 1   # decrementing the number by 1 otherwise it will be infinite loop

print(fact)