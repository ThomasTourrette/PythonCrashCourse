#!/usr/bin/env

# READING A FILE

# with keyword close the file when the file is not needed anymore
#with open('pi_digits.txt') as file_object:
#    #contents = file_object.read()
#    lines = file_object.readlines() # store line in a list
#    #print(contents.rstrip())
#
#pi_str = ''
#for line in lines:
#    print(line)
#    pi_str += line.rstrip()
#
#
#print(pi_str)
#
#
#birthday = input("what is your age ? ")
#if birthday in pi_str:
#    print("your birthday is in pi")
#else:
#    print("your birthday is not in pi")


# WRITING TO A FILE
file_name = 'programing.txt'

# openning mode:
# w: write mode
# a: append mode
# r+: read/write mode
with open(file_name, 'w') as file_object:
    file_object.write("I love programming")



