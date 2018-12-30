#/usr/bin/env


# Exception are handled with try/except bloc


#while True:
#    numerateur = input("numérateur: ")
#    if "q" == numerateur:
#        break
#    denominateur = input("dénominateur: ")
#    try:
#        result = int(numerateur)/int(denominateur)
#    except ZeroDivisionError:
#        print("You cant divide by zero!")
#    else:
#        print(result)

# FileNotFoundError



# Storing data JSON


import json


numbers = [number**2 for number in range(1, 7)]
filename = "save.json"

with open(filename, "w") as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    numbers2 = json.load(f_obj)

print(numbers2)

