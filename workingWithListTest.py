#!/usr/bin/env
from utilsTest import printListInteger
from utilsTest import printList

magicians = ["thomas", "john", "robert"]
for magician in magicians:
    print(magician)

for value in range (1, 5):
    print(value)

# Making a list of numbers
numbers = list(range(1, 6))
print(numbers)

# List of even numbers
evenNumbers = list(range(0, 12, 2))
print(evenNumbers)


# List of squares values
squares = []
for value in range(1, 5):
    squares.append(value*value)

printListInteger(squares)


# Statistics with list
print(squares)
print(max(squares))
print(min(squares))
print(sum(squares))

# List comprehension
squares = [value**2 for value in range(1,5)]
printListInteger(squares)

# Part of a list (slice)
players = ['thomas', 'jean', 'vincent', 'florian', 'eli']

printList(players[0:3])

# Make a copy
players2 = players[:]
players2.append("laura")
printList(players)
printList(players2)

# Tuples (immutable list)
fruits = ('pomme', 'orange', 'poire')
fruits = ('pomme', 'orange', 'poire', 'banane')
fruitsList = [fruit for fruit in fruits]
printList(fruitsList)


