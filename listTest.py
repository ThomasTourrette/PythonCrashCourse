#!/usr/bin/env
from utilsTest import printList
import copy



cars = ['clio', 'corolla', 'almera']
# Add elements to a list
cars.append("octavia")
cars.insert(2, "classe C")
printList(cars)

# copy list
cars2 = cars.copy()
cars3 = list(cars)
cars4 = copy.copy(cars)

# Removing element from list
del cars[0]
cars.pop() # without argument pop the last item
cars.remove("almera")
printList(cars)

cars2.sort()
printList(cars2)

# Sort list
cars3.sort(reverse=True)
printList(sorted(cars3))
printList(cars3)

cars3.reverse()
printList(cars3)
