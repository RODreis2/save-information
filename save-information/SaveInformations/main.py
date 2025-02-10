import sys
import os

#List and dict that will store
list_one = []
dict_one = {}

print("=" * 83)
print("we application is a list and a dictionary to which you will add values in the sames")
print("=" * 83)

#start of the program
while True:

    #Fist part: where you will save your things, clean or Help(only if you don't know what the program does).
    FistChosen = input("Chose option \n"
                  "[L]ist [D]ictionary [H]elp : ")


    #____LIST PART____
    os.system('clear')
    if FistChosen.upper() == "L":
        ListChosen = input("Chose option \n"
                    "[I]nsert [L]ist [D]elete [C]lean [E]xit: ")


        #List: insert logic 
        os.system('clear')
        if ListChosen.upper() == 'I':
            shopping = input("write value: ")
            os.system('clear')
            list_one.append(shopping)

        #List: delete logic
        elif ListChosen.upper() == 'D':
            os.system('clear')
            ChoseToDelete = int(input("Write number of information that you want to delete: "))
            try:
                list_one.pop(ChoseToDelete)
            except:
                os.system('clear')
                print(f"The number do not be in the list, write again please.")
                continue
        
        #List: list logic
        elif ListChosen.upper() == 'L':
            os.system('clear')
            for value, index in enumerate(list_one):
                print(f"{value} {index}")

        #List: Exit logic
        elif ListChosen.upper() == "E":
            os.system('clear')
            print("thank you for use we aplication byeee ")
            sys.exit()

        #List: Clean logic
        elif ListChosen.upper() == 'C':
            os.system('clear')
            list_one.clear()
            print("List has been cleaned.")
        
        else:
            print("Write again please.")
            continue


    #____DICTIONARY PART____
    elif FistChosen.upper() == "D":
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
                continue

        #Dict: Show logic
        elif DictChosen.upper() == "S":
            for value3, index4 in enumerate(dict_one):
                print(f"{value3}: {index4}")

        #Dict: Clean logic
        elif DictChosen.upper() == "C":
            os.system('clear')
            sure = str(input("Are you sure? [Y]es [N]o "))
            if sure.upper() == "Y": 
                os.system('clear')
                dict_one.cear()
                print("Dict has been cleaned.")            

        #Dict: Exit logic
        elif DictChosen.upper() == "E":
            os.system('clear')
            print("thank you for use we app byeee :)")
            sys.exit()


    #____HELP PART____
    elif FistChosen.upper() == "H":
        print("LIST: a list is like a container that holds a bunch of items. \n"
              "These items can be numbers, text, or even other lists. \n"
              "Lists keep things in a particular order, so you can find them later by their position in the list. \n"
              "You can add or remove items from a list, change the items in it, or check if an item is inside it.")

        print("\nDICT: You can think of a dictionary as a collection of labeled compartments,\n"
              "where each compartment (value) is associated with a unique label (key).\n"
              "These labels can be strings, numbers, or even tuples, while the values can be any data type,\n"
              "including numbers, strings, lists, or even other dictionaries.")
