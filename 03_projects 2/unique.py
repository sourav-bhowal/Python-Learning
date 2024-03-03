fruits = ["apple", "orange", "banana", "orange", "pineapple", "apple"]

unique_fruit = []

for fruit in fruits:
    if fruit in unique_fruit:
        print("Duplicate fruit:", fruit)
        continue
    unique_fruit.append(fruit)

print(unique_fruit) 