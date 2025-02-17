import os
list_one = []
def Listfunction():
    ListChosen = input("Chose option \n"
                    "[I]nsert [L]ist [D]elete [C]lean [E]xit: ")
    os.system('clear')
    if ListChosen.upper() == 'I':
            shopping = input("write value: ")
            os.system('clear')
            list_one.append(shopping)

        #List: delete logic
    elif ListChosen.upper() == 'D':
            os.system('clear')
            for tup in list_one:
                for index, item in enumerate(list_one):
                    print(f"{index}: {item},")

            ChoseToDelete = int(input("Write number of information that you want to delete: "))
            try:
                list_one.pop(ChoseToDelete)
            except:
                os.system('clear')
                print(f"The number do not be in the list, write again please.")
                quit()        
                
        #List: list logic
    elif ListChosen.upper() == 'L':
            os.system('clear')
            for tup in list_one:
                num, item = tup[0], tup[1]  # Only using the first two elements
                print(f"{num}: {item}")


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
            
