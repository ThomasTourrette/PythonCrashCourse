#!/usr/bin/env

from utilsTest import printDico

alien_0 = {'color': 'green', 'points': 5}
alien_0['age'] = 28
print(alien_0['color'])
print(alien_0['points'])
print(alien_0['age'])

alien_0['speed'] = 'fast'
print(alien_0)
del alien_0['speed']
print(alien_0)

# Looping through key/value pairs
for k, v in alien_0.items():
    print(str(k) + ": " + str(v))

# Looping through keys
for key in alien_0.keys():
    print(key)

# Looping through values
for value in alien_0.values():
    print(value)

# Nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 7}
alien_2 = {'color': 'blue', 'points': 3}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# Generate aliens
aliens = []

for n in range(30):
    aliens.append(alien_0)

for alien in aliens[:5]:
    print(alien)

print("number of aliens:" + str(len(aliens)))

