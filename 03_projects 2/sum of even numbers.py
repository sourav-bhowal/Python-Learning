n = 10
sum = 0

for number in range(1, n+1):
    if number%2 == 0:
        sum += number

print("Sum of even numbers: ",sum)