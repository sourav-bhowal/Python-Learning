#### CLASS ####
class Car:
    #### CLASS VARIABLE ####
    total_car = 0   # holds how many cars/objects are created

    #### __INIT__ FUNCTION (special fn) ####
    def __init__(self, brand, model):
        self.__brand = brand  # "self" is used for the variable of the function similar to "this" in javascript
        self.__model = model  # "__model or __brand" makes the variable private
        Car.total_car += 1  # "or" self.total_car += 1 , EVERY TIME A NEW CAR/OBJECT IS CREATED DO +1

    #### NORMAL FUNCTION ####
    def car_fullname(self): # "self" is used to connect the fn to the above __init__ function
        return f"{self.__brand} {self.__model}"
    
    #### ENCAPSULATION ####
    def get_brand(self):    # getter for the brand as its a private property
        return self.__brand + " !!!"

    #### POLYMORPHISM ####
    def fuel_type(self):
        return "Petrol or Diesel"
    
    #### STATIC METHOD ####
    @staticmethod   # we dont need static when its a static method as we dont need wiring
    def general_description():
        return "Cars are good for transportation"

    #### PROPERTY DECORATOR ####
    @property
    def model(self):
        return self.__model

#### INHERITENCE ####
class ElectricCar(Car): # "ElectricCar" is accesing the above "Car" class and inheriting everything from it
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # super().__init__() is used to access the above declared variables (brand and model)
        self.battery_size = battery_size

    #### POLYMORPHISM ####
    def fuel_type(self):
        return "Electric Charge"
    
################################################################################################
    
# my_car1 = Car("Ford", "Mustang")
# print(my_car1.get_brand())
# print(my_car1.model)
# print(my_car1.fuel_type())

# my_car2 = Car("Tata", "NEXON")
# print(my_car2.model)
# print(my_car2.get_brand())
# print(my_car2.car_fullname())   # calling my_car2.car_fullname function so we need parenthesis

################################################################################################

# my_car3 = ElectricCar("Tesla", "Model S", "90kWh")

#### INSTANCE CHECK ####
# print(isinstance(my_car3, Car))
# print(isinstance(my_car3, ElectricCar))

# print(my_car3.model)
# print(my_car3.car_fullname())
# print(my_car3.battery_size)
# print(my_car3.get_brand())
# print(my_car3.fuel_type())
    
################################################################################################

# print(Car.total_car)    # total_car can be accessed through the "Car" class
# print(Car.general_description())    # general_descp can be accessed through the "Car" class

################################################################################################

#### MULTIPLE INHERITENCE ####       
class Battery:
    def battery_info(self):
        return "This is the battery"

class Engine:
    def engine_info(self):
        return "This is the engine"

class ElectricTruck(Battery, Engine, Car):
    pass

# my_cybertruck = ElectricTruck("Tesla", "CyberTruck")

# print(my_cybertruck.battery_info())
# print(my_cybertruck.engine_info())
# print(my_cybertruck.model)