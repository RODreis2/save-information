from Documentation import Documentation
from ListLogic import Listfunction
from DictLogic import DictFunction
import sys
import os


#List and dict that will store

def init():
    if FistChosen.upper() == "L":
        return Listfunction()
    elif FistChosen.upper() == "D":
        return DictFunction()
    elif FistChosen.upper() == "H":
        return Documentation()

print("=" * 83)
print("we application is a list and a dictionary to which you will add values in the sames")
print("=" * 83)

#start of the program
while True:

    #Fist part: where you will save your things, clean or Help(only if you don't know what the program does).
    FistChosen = input("Chose option \n"
                  "[L]ist [D]ictionary [H]elp : ")

    init()