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
    options = input("Chose option \n"
                  "[L]ist [D]ictionary [C]lean [H]elp : ")

    #LIST PART
    if options.upper() == "L":
        chose1 = input("Chose option \n"
                    "[I]nsert [D]elet [L]ist [E]xit: ")

        if chose1.upper() == 'I':
            shopping = input("write value: ")
            list_one.append(shopping)

        elif chose1 == 'D' or chose1 == 'd':

            Chose1_5 = int(input("Write number you want to delete: "))
            try:
                list_one.pop(Chose1_5)
            except:
                print(f"The number do not be in the list, write again please.")
                continue

        elif chose1 == 'L' or chose1 == 'l':
            for value, index in enumerate(list_one):
                print(f"{value} {index}")

        elif chose1 == "e" or chose1 == "E":
            print("thank you for use we app byeee :)")
            sys.exit()

    #DICTIONARY PART
    elif options == "D" or options == "d":
        chose2 = input("Chose option \n"
                      "[I]nsert [D]elet [S]how [E]xit: ")

        if chose2 == "I" or chose2 == "i":
            name_dict2 = input("Write name: ")
            description = input("Write description: ")
            dict_one.update({name_dict2: description})

        elif chose2 == "D" or chose2 == "d":
            for value2, index2 in dict_one.items():
                print(f"{value2} {index2}")
            Chose2_5 = input("Write name you want to delete: ")
            try:
                del dict_one[Chose2_5]
            except:
                print(f"The name do not be in the dictionary, write again please.")
                continue

        elif chose2 == "S" or chose2 == "s":
            for value3, index3 in enumerate(dict_one):
                print(f"{value3} {index3}")

        elif chose2 == "e" or chose2 == "E":
            print("thank you for use we app byeee :)")
            sys.exit()

    #HELP PART
    elif options == "H" or options == "h":
        print("LIST: a list is like a container that holds a bunch of items. \n"
              "These items can be numbers, text, or even other lists. \n"
              "Lists keep things in a particular order, so you can find them later by their position in the list. \n"
              "You can add or remove items from a list, change the items in it, or check if an item is inside it.")

        print("\nDICT: You can think of a dictionary as a collection of labeled compartments,\n"
              "where each compartment (value) is associated with a unique label (key).\n"
              "These labels can be strings, numbers, or even tuples, while the values can be any data type,\n"
              "including numbers, strings, lists, or even other dictionaries.")


    #CLEAN PART
    elif options == "c" or options == "C":
        print("we can't use this function now, sorry :")
    else:
        print("Please select just correct options")
        continue