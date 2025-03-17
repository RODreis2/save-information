import curses

dict_one = {}

def DictFunction(stdscr):
    stdscr.clear()
    stdscr.addstr("Choose option:\n")
    stdscr.addstr("[I]nsert [S]how [D]elete [C]lean [E]xit: ")
    stdscr.refresh()
    choice = stdscr.getch()
    
    if chr(choice).upper() == "I":
        DictFunctionInsert(stdscr)
    elif chr(choice).upper() == "S":
        DictFunctionShow(stdscr)
    elif chr(choice).upper() == "D":
        DictFunctionDelete(stdscr)
    elif chr(choice).upper() == "C":
        DictFunctionClean(stdscr)
    elif chr(choice).upper() == "E":
        DictFunctionExit()


def DictFunctionInsert(stdscr):
    from Display import get_input
    """Função para inserir dados no dicionário usando a função get_input."""
    name_dict2 = get_input(stdscr, "Write name: ")  # Chama a função para capturar o nome
    if name_dict2 is None:
        return  # Se o usuário pressionar ESC, sai da função

    description = get_input(stdscr, "Write description: ")  # Chama a função para capturar a descrição
    if description is None:
        return  # Se o usuário pressionar ESC, sai da função
    
    dict_one.update({name_dict2: description})  # Atualiza o dicionário com os dados inseridos

    # Exibe uma confirmação
    stdscr.clear()
    stdscr.addstr(0, 0, f"Added '{name_dict2}' with description: '{description}'")
    stdscr.refresh()
    stdscr.getch()  # Espera o usuário pressionar uma tecla para continuar


def DictFunctionDelete(stdscr):
    from Display import get_input
    stdscr.clear()
    for i, (key, value) in enumerate(dict_one.items()):
        stdscr.addstr(i, 0, f"{key}: {value}")
        
    DelName = get_input(stdscr, "Write the name you want to delete: ", len(dict_one) + 1, 0)
    
    if DelName in dict_one:
        del dict_one[DelName]
        stdscr.addstr(len(dict_one) + 2, 0, f"'{DelName}' deleted successfully!")
    else:
        stdscr.addstr(len(dict_one) + 2, 0, "The name is not in the dictionary. Press any key to continue...")

    stdscr.refresh()
    stdscr.getch()

def DictFunctionShow(stdscr):
    stdscr.clear()
    for i, (key, value) in enumerate(dict_one.items()):
        stdscr.addstr(i, 0, f"{key}: {value}")
    stdscr.addstr(len(dict_one), 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

def DictFunctionClean(stdscr):
    stdscr.clear()
    stdscr.addstr("Are you sure? [Y]es [N]o: ")
    stdscr.refresh()
    choice = stdscr.getch()
    if chr(choice).upper() == "Y":
        dict_one.clear()
        stdscr.addstr("Dict has been cleaned. Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()

def DictFunctionExit():
    from Logics.ExitLogic import fullExit
    fullExit()

def main():
    curses.wrapper(DictFunction)

if __name__ == "__main__":
    main()
