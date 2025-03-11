import os
import sys
list_one = []
def Listfunction():
    ListChosen = input("Chose option \n"
                    "[I]nsert [L]ist [D]elete [C]lean [E]xit: ")
    
    os.system('clear' if os.name == 'posix' else 'cls')    
    if ListChosen.upper() == 'I':
        return ListfunctionInsert()
    
    elif ListChosen.upper() == "D":
        return ListFunctionDelete()
    
    elif ListChosen.upper() == "L":
        return Listfunctionlist()

    elif ListChosen.upper() == "C":
        return ListfunctionClear()
    
    elif ListChosen.upper() == "E":
        return ListfunctionExit()

    else:
        print("Write again please.")

def ListfunctionInsert():
            shopping = input("write value: ")
            os.system('clear' if os.name == 'posix' else 'cls')
            list_one.append(shopping)

def ListFunctionDelete():
        #List: delete logic
            os.system('clear' if os.name == 'posix' else 'cls')
            for index, item in enumerate(list_one):
                print(f"{index}: {item},")

            ChoseToDelete = int(input("Write number of information that you want to delete: ").strip())
            try:
                list_one.pop(ChoseToDelete)
            except:
                os.system('clear' if os.name == 'posix' else 'cls')
                print(f"The number do not be in the list, write again please.")
                quit()        
                
def Listfunctionlist():
        #List: list logic
        os.system('clear' if os.name == 'posix' else 'cls')
        for index, item in enumerate(list_one):
            print(f"{index}: {item}")


    #List: Exit logic
def ListfunctionExit():
            from Logics.ExitLogic import fullExit
            fullExit()

def ListfunctionClear():
            os.system('clear' if os.name == 'posix' else 'cls')
            list_one.clear()
            print("List has been cleaned.")
        
            