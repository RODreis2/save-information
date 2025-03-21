import os
import sys
import curses

# Certifique-se de que a pasta 'logics' esteja no mesmo diretório ou que você adicione ao sys.path se estiver em outro local
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Adiciona o diretório atual ao sys.path

list_one = []

def Listfunction(stdscr):
    stdscr.clear()
    stdscr.addstr("Choose option:\n")
    stdscr.addstr("[I]nsert [S]how [D]elete [C]lean [E]xit: ")
    stdscr.refresh()
    Lchoice = stdscr.getch()
    Lchoice_char = chr(Lchoice).upper()  # Converte o código da tecla para um caractere

    if Lchoice_char == 'I':
        ListfunctionInsert(stdscr)
    elif Lchoice_char == "D":
        ListFunctionDelete(stdscr)
    elif Lchoice_char == "L":
        Listfunctionlist(stdscr)
    elif Lchoice_char == "C":
        ListfunctionClear(stdscr)
    elif Lchoice_char == "E":
        ListfunctionExit(stdscr)
    else:
        stdscr.addstr("Invalid option. Try again.\n")
        stdscr.refresh()
        stdscr.getch()

def ListfunctionInsert(stdscr):
    from Logics.Display import get_input  # Certifique-se de que o método get_input está implementado corretamente
    from Logics.ExitLogic import fullExit  # Certifique-se de que fullExit está implementado corretamente

    shopping = get_input(stdscr, "Write value: ")
    list_one.append(shopping)

    # Exibe uma confirmação
    stdscr.clear()
    stdscr.addstr(f"Added '{shopping}' to the list.\n")
    stdscr.refresh()
    stdscr.getch()

def ListFunctionDelete(stdscr):
    stdscr.clear()
    for i, item in enumerate(list_one):
        stdscr.addstr(i, 0, f"{i}: {item}")
    stdscr.refresh()

    DelName = get_input(stdscr, "Write the name you want to delete: ")

    if DelName in list_one:
        list_one.remove(DelName)
        stdscr.addstr(len(list_one) + 2, 0, f"'{DelName}' deleted successfully!")
    else:
        stdscr.addstr(len(list_one) + 2, 0, "The name is not in the list. Press any key to continue...")

    stdscr.refresh()
    stdscr.getch()

def Listfunctionlist(stdscr):
    stdscr.clear()
    for i, item in enumerate(list_one):
        stdscr.addstr(i, 0, f"{i}: {item}")
    stdscr.refresh()
    stdscr.getch()

def ListfunctionClear(stdscr):
    stdscr.clear()
    stdscr.addstr("Are you sure? [Y]es [N]o: ")
    stdscr.refresh()
    choice = stdscr.getch()
    if chr(choice).upper() == "Y":
        list_one.clear()
        stdscr.addstr("List has been cleaned. Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()
    
def ListfunctionExit(stdscr):
    from Logics.ExitLogic import fullExit  # Certifique-se de que o método fullExit está implementado corretamente
    fullExit(stdscr)
