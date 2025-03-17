import curses
from Documentation import Documentation
import SavePdf  # Se necessário
import Logics.DictLogic
import Logics.ListLogic
import Logics.ExitLogic


def init(FistChosen, stdscr):
    """Chama a função correspondente à opção escolhida"""
    if FistChosen.upper() == "L":
        Logics.ListLogic.Listfunction(stdscr)
    elif FistChosen.upper() == "D":
        Logics.DictLogic.DictFunction(stdscr)
    elif FistChosen.upper() == "H":
        Logics.DictLogic.Documentation(stdscr)
    elif FistChosen.upper() == "E":
        Logics.fullExit()
    elif FistChosen.upper() == "I":
        # Implementar lógica de "I" se necessário
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
        option_text = "[L]ist [D]ictionary [H]elp [I]mage [E]xit: "
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
