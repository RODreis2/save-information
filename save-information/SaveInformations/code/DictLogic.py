import os
import sys
dict_one = {}

def DictFunction():
    DictChosen = input("Chose option \n"
                      "[I]nsert [S]how [D]elete [C]lean [E]xit: ")
    if DictChosen.upper() == "I":
        return DictFunctionInsert()
    elif DictChosen.upper() == "S":
        return DictFunctionShow()
    elif DictChosen.upper() == "D":
        return DictFunctionDelete()
    elif DictChosen.upper() == "C":
        return DictFunctionDelete()
    elif DictChosen.upper() == "E":
        return DictFunctionExit()
     

    #Dict: insert logic
def DictFunctionInsert():
        os.system('clear')
        name_dict2 = input("Write name: ")
        description = input("Write description: ")
        dict_one.update({name_dict2: description})

    #Dict: Delete logic
def DictFunctionDelete():
        os.system('clear')
        for value1, index2 in dict_one.items():
                print(f"{value1} {index2}")
        DictItemDelete = input("Write name you want to delete: ")
        try:
            del dict_one[DictItemDelete]
        except:
            os.system('clear')
            print(f"The name do not be in the dictionary, write again please.")
            

    #Dict: Show logic
def DictFunctionShow():
        os.system('clear')
        for value3, index4 in dict_one.items():
                print(f"{value3}: {index4}")

    #Dict: Clean logic
def DictFunctiontClean():
        os.system('clear')
        sure = str(input("Are you sure? [Y]es [N]o "))
        if sure.upper() == "Y": 
            os.system('clear')
            dict_one.clear()
            print("Dict has been cleaned.")            

    #Dict: Exit logic
def DictFunctionExit():
        os.system('clear')
        print("thank you for use we app byeee :)")
        sys.exit()
