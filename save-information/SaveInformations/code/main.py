import curses
import SavePdf
from Logics.Documentation import documentation
import Logics.DictLogic
import Logics.ListLogic
import Logics.ExitLogic
from EncryptImVid import encrypt_file
from DecryptImVid import decrypt_file

def init(FistChosen, stdscr):
    """Chama a função correspondente à opção escolhida"""
    if FistChosen.upper() == "L":
        Logics.ListLogic.Listfunction(stdscr)
    elif FistChosen.upper() == "D":
        Logics.DictLogic.DictFunction(stdscr)
    elif FistChosen.upper() == "H":
        documentation(stdscr)
    elif FistChosen.upper() == "Q":
        Logics.ExitLogic.fullExit(stdscr)
    elif FistChosen.upper() == "E":
        stdscr.clear()
        options = "[E]ncrypt [D]ecrypt [Q]uit"
        center_text(stdscr, options, 2)
        stdscr.refresh()
        Enchoose = stdscr.getch()
        Enchoose_char = chr(Enchoose).upper()
        while True:
            if Enchoose_char == "E":
                encrypt_file(stdscr) 
            elif Enchoose_char == "D":
                decrypt_file(stdscr)
            elif Enchoose_char == "Q":
                break

        pass

def center_text(stdscr, text, row):
    """Centraliza o texto na tela"""
    col = (curses.COLS - len(text)) // 2
    stdscr.addstr(row, col, text)

def main(stdscr):
    """Função principal que executa o menu e gerencia a entrada do usuário"""
    # Inicializa o Ncurses
    curses.curs_set(1)  # Oculta o cursor
    stdscr.clear()  # Limpa a tela
    stdscr.refresh()

    while True:    # Exibindo a introdução do programa
        center_text(stdscr, "=" * 82, 0)
        center_text(stdscr, "We application is a list and a dictionary to which you will add values in the same", 1)
        center_text(stdscr, "=" * 82, 2)
        stdscr.refresh()

        # Exibindo as opções de escolha, centralizado
        option_text = "[L]ist [D]ictionary [H]elp [E]ncrypt/Decrypt [Q]uit: "
        center_text(stdscr, option_text, 4)
        stdscr.refresh()
        FistChosen = stdscr.getch()
        FistChosen_char = chr(FistChosen).upper()

        init(FistChosen_char, stdscr)
        # Chama a função init com a escolha do usuário
    

        # Limpa a tela antes de reexibir as opções
        stdscr.clear()

if __name__ == "__main__":
    curses.wrapper(main)
