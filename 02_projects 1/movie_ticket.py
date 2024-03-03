age = int(input('Enter the age:'))
day = input('Day of the week:')

price = 12 if age>=18 else 8

if day == "wednesday":
    price = price - 2

print(f"Price of the ticket for {day} is ${price}")