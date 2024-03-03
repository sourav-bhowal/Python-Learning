userAge = int(input("Enter your age: "))

if userAge < 13:
    print("You are a child")
elif (userAge >= 13 and userAge <=19):
    print("You are a Tennager")
elif (userAge >=20 and userAge <=59):
    print("You are a Adult")
else:
    print("You are a Senior")
           