#!/usr/bin/env

def greet_user(user):
    print("hello " + str(user))


greet_user("thomas")


# Default argument
def decribe_pet(name, race="dog"):
    print(str(name).title() + " is a " + str(race))

decribe_pet("joe")
decribe_pet("joe", "elephant")


# Making an argument optional
#def decribe_pet(name, race=""):

# Returning dictionnaries

def buildPerson(first_name, last_name, age=''):
    person = {'first': first_name.title(), 'last': last_name.title()}
    if age:
        person['age'] = age
    return person


p1 = buildPerson("thomas", "tourrette", 30)
print(p1)


v = 2
def functionTest(value):
    value = value*100
    return value

result = functionTest(v)
print(v)
print(result)

# Preventing function from modifying a list
list1 = [1, 2, 3]
def testList(list_t):
    list_t.append(4)
testList(list1[:])
print(list1)


# Passing an arbitrary number of arguments



