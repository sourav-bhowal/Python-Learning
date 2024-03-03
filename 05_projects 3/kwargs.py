def handle(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


handle(name = "Sourav")
handle(name = "Sourav", age = 20)
handle(name = "Sourav", age = 20, degree = "CSE")