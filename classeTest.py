#!/usr/bin/env

# A class
class Dog():
    """ Class representing a dog """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """ Simulating a dog sitting in response to a command """
        print(self.name + " is now sitting.")

    def roll_over(self):
        """ Simulating rolling over in response to a command """
        print(self.name + " rolled over !")


my_dog = Dog("joe", 10)
my_dog.sit()
my_dog.roll_over()


# Inheritance

class YellowDog(Dog):
    def __init__(self, name, age, master, color="yellow"):
        super().__init__(name, age)
        self.color = color
        self.master = master
    def print_infos(self):
        print(self.name.title() + " appartient à " + master.name.title())

class Master():
    def __init__(self, name, age):
        self.name = name
        self.age = age

master = Master("john", 30)
yellow_dog = YellowDog("Yellow", 20, master)
yellow_dog.sit()
yellow_dog.roll_over()
yellow_dog.print_infos()


