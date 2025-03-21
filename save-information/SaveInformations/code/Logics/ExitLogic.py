import os
import sys
import curses
from SavePdf import save_to_pdf
from Logics.ListLogic import list_one
from Logics.DictLogic import dict_one

def exitClear1(stdscr):
    """Limpa a tela e encerra o programa com uma mensagem de despedida."""
    stdscr.clear()
    stdscr.addstr("Thank you for using our application. Byeee!\n")
    stdscr.refresh()
    stdscr.getch()
    sys.exit()


def fullExit(stdscr):
    from Logics.ListLogic import list_one
    from Logics.DictLogic import dict_one

    """Pergunta ao usuário se deseja salvar as informações e encerra o programa."""
    stdscr.clear()
    stdscr.addstr("Do you wanna save your information [S/N]? ")
    stdscr.refresh()

    while True:
        SaveOrNot = chr(stdscr.getch()).strip().upper()  # Captura a tecla pressionada
        stdscr.clear()

        if SaveOrNot == "S":    
            namefile = get_input(stdscr, "Write the name: ").strip()
            try:
                save_to_pdf(stdscr, namefile, list_one, dict_one)
                exitClear1(stdscr)  # Chama a função para finalizar o programa
            except Exception as e:  # Alterado para capturar qualquer erro
                stdscr.addstr(f"Error: {e}\n")
                stdscr.refresh()
                stdscr.getch()
                continue 

        elif SaveOrNot == "N":
            exitClear1(stdscr)
        
        else:
            stdscr.addstr("Invalid input. Please enter 'S' or 'N'.\n")
            stdscr.refresh()
            stdscr.getch()


def get_input(stdscr, prompt, row=0, col=0):
    """Captura a entrada do usuário com Ncurses."""
    stdscr.clear()
    stdscr.addstr(row, col, prompt)
    stdscr.refresh()
    
    input_str = ""
    while True:
        stdscr.clear()
        stdscr.addstr(row, col, prompt)
        stdscr.addstr(row + 1, col, "You are typing: " + input_str)
        stdscr.refresh()
        
        key = stdscr.getch()

        if key == 10:  # Se pressionar ENTER
            break
        elif key == 27:  # Se pressionar ESC
            return None
        elif key == 263:  # Se pressionar BACKSPACE
            input_str = input_str[:-1]
            col -= 1  # Corrige a posição do cursor
        else:
            input_str += chr(key)
            col += 1  # Avança a posição do cursor

    return input_str
