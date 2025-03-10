from ListLogic import list_one
from DictLogic import dict_one
from SavePdf import save_to_pdf
import os
import sys


def exitClear1():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("Thank you for using our application. Byeee! ")
    sys.exit()


def fullExit():
    while True:
        SaveOrNot = input("Do you wanna save your information [S/N]? ").strip().upper()
        
        if SaveOrNot == "S":
            namefile = input("Write the name: ").strip()
            try:
                save_to_pdf(namefile, list_one, dict_one)  
                exitClear1()
            except NameError as e:
                print(f"Error: {e}")  
                continue 

        elif SaveOrNot == "N":
            exitClear1()
        
        else:
            print("Invalid input. Please enter 'S' or 'N'.")  