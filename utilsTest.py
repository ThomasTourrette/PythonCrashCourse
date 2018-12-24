#!/usr/bin/env


def printList(list):
    print("Items in list (len: %d):"% len(list))
    for item in list:
        print("\t - " + item)

def printListInteger(list):
    print("Items in list (len: %d):"% len(list))
    for item in list:
        print("\t - " + str(item))

def printDico(dictionarie):
    print("Items in dictionarie (len: %d):"% len(dictionarie))
    for k, v in dictionarie.items():
        print("\t - " + "[" + str(k) + "]: " + str(v))

