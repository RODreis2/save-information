import os
import sys
dict_one = {}

def DictFunction():
    DictChosen = input("Chose option \n"
                      "[I]nsert [S]how [D]elete [C]lean [E]xit: ")

        #Dict: insert logic
    if DictChosen.upper() == "I":
        os.system('clear')
        name_dict2 = input("Write name: ")
        description = input("Write description: ")
        dict_one.update({name_dict2: description})

        #Dict: Delete logic
    elif DictChosen.upper() == "D":
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
    elif DictChosen.upper() == "S":
        os.system('clear')
        for value3, index4 in dict_onel.items():
                print(f"{value3}: {index4}")

        #Dict: Clean logic
    elif DictChosen.upper() == "C":
        os.system('clear')
        sure = str(input("Are you sure? [Y]es [N]o "))
        if sure.upper() == "Y": 
            os.system('clear')
            dict_one.clear()
            print("Dict has been cleaned.")            

        #Dict: Exit logic
    elif DictChosen.upper() == "E":
        os.system('clear')
        print("thank you for use we app byeee :)")
        sys.exit()
