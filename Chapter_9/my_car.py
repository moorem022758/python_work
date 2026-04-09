# Importing serval Classes


"""A set of classes used to represent gas and electric cars."""
# from car import Car, ElectricCar

"""This imports the module"""
# import car

"""This imports all Classes from a module"""
from car import * 

"""This imports class using an Aliases"""
from electric_car import ElectricCar as EC

"""This imports the module and uses Aliases"""
import electric_car as ec


# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_mustang = Car('ford', 'mustang', 2024)
# my_mustang = car.Car('ford', 'mustang', 2024)
my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_leaf = EC('nissan', 'leaf', 2026)
print(my_leaf.get_descriptive_name())

my_leaf = ec.ElectricCar('nissan', 'leaf', 2027)
print(my_leaf.get_descriptive_name())
