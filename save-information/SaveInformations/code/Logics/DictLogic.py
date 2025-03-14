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

import curses

def DictFunctionInsert(stdscr):
    stdscr.clear()
    
    # Exibe a instrução de digitação para o nome
    stdscr.addstr(0, 0, "Write name: ")
    stdscr.refresh()
    name_dict2 = ""
    
    # Captura a entrada de texto enquanto o usuário digita
    while True:
        stdscr.addstr(1, 0, "You are typing: " + name_dict2)  # Exibe o que o usuário está digitando
        stdscr.refresh()
        key = stdscr.getch()  # Captura a tecla pressionada
        
        # Se pressionar ENTER (código 10), sai do loop
        if key == 10:
            break
        elif key == 27:  # Se pressionar ESC (código 27), sai do loop
            return
        elif key == 263:  # Se pressionar BACKSPACE (código 263), remove o último caractere
            name_dict2 = name_dict2[:-1]
        else:
            name_dict2 += chr(key)  # Adiciona o caractere digitado à string

    # Agora, pede pela descrição
    stdscr.clear()
    stdscr.addstr(0, 0, "Write description: ")
    stdscr.refresh()
    description = ""
    
    # Captura a entrada da descrição enquanto o usuário digita
    while True:
        stdscr.addstr(1, 0, "You are typing: " + description)  # Exibe o que o usuário está digitando
        stdscr.refresh()
        key = stdscr.getch()  # Captura a tecla pressionada
        
        # Se pressionar ENTER (código 10), sai do loop
        if key == 10:
            break
        elif key == 27:  # Se pressionar ESC (código 27), sai do loop
            return
        elif key == 263:  # Se pressionar BACKSPACE (código 263), remove o último caractere
            description = description[:-1]
        else:
            description += chr(key)  # Adiciona o caractere digitado à string

    # Atualiza o dicionário com o nome e a descrição fornecidos
    dict_one.update({name_dict2: description})

    # Exibe uma confirmação
    stdscr.clear()
    stdscr.addstr(0, 0, f"Added '{name_dict2}' with description: '{description}'")
    stdscr.refresh()
    stdscr.getch()  # Espera o usuário pressionar uma tecla para continuar


def DictFunctionDelete(stdscr):
    stdscr.clear()
    for i, (key, value) in enumerate(dict_one.items()):
        stdscr.addstr(i, 0, f"{key}: {value}")
    stdscr.addstr(len(dict_one), 0, "Write name you want to delete: ")
    stdscr.refresh()
    
    DictItemDelete = stdscr.getstr().decode("utf-8")
    if DictItemDelete in dict_one:
        del dict_one[DictItemDelete]
    else:
        stdscr.addstr(len(dict_one) + 1, 0, "The name is not in the dictionary, press any key to continue...")
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
