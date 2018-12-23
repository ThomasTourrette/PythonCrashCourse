#!/usr/bin/env

from utilsTest import printList

cars = ["renault", "peugeot", "bmw"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# Check multiple condition with 'and' and 'or'
cars.append("subaru")
cars.insert(2, "audi")
cars.insert(0, "renault")

printList(cars)
if cars[0] == cars[1] or cars[2] == "bmw":
    print("test pass")
else:
    print("test failed")

# Check if value is 'in' or 'not in' a list
if "renault" in cars:
    print("there is a renault")
if "porsche" in cars:
    print("there is a porsche")

if "porsche" in cars and "renault" in cars:
    print("il y une porche et une renault")




