from Documentation import Documentation
from SavePdf import save_to_pdf
import Logics.DictLogic
import Logics.ListLogic 
import Logics.ExitLogic
import sys
import os


def init():
    if FistChosen.upper() == "L":
        return Logics.ListLogic.Listfunction()
    elif FistChosen.upper() == "D":
        return Logics.DictLogic.DictFunction()
    elif FistChosen.upper() == "H":
        return Logics.DictLogic.Documentation()
    elif FistChosen.upper() == "E":
        return Logics.fullExit()
        


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
    