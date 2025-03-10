from Documentation import Documentation
from ListLogic import Listfunction
from DictLogic import DictFunction
from SavePdf import save_to_pdf
from ExitLogic import exitClear1
from ExitLogic import fullExit
import sys
import os


def init():
    if FistChosen.upper() == "L":
        return Listfunction()
    elif FistChosen.upper() == "D":
        return DictFunction()
    elif FistChosen.upper() == "H":
        return Documentation()
    elif FistChosen.upper() == "E":
        return fullExit()
        


print("=" * 83)
print("we application is a list and a dictionary to which you will add values in the sames")
print("=" * 83)

#start of the program
while True:

    #Fist part: where you will save your things, clean or Help(only if you don't know what the program does).
    FistChosen = input("Chose option \n"
                  "[L]ist [D]ictionary [H]elp [E]xit: ")


    #Start
    init()
    