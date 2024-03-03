import math

def area(radius):
    return math.pi * (radius**2)

def circumference(radius):
    return 2 * math.pi * radius

radius = int(input("Enter radius: "))

result1 = area(radius)
result2 = circumference(radius)

print(f"Area of circle: {result1:.2f} \nCircumference of circle: {result2:.2f}")