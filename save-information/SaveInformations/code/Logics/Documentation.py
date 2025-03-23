import os
import curses


def center_text(stdscr, text, row):
    """Centraliza o texto na tela"""
    col = (curses.COLS - len(text)) // 2
    stdscr.addstr(row, col, text)

#____HELP PART____
def docTitle(stdscr):
    stdscr.clear()
    title_lines = [
        "=" * 83,
        "------------------------------------ Hello Guys -----------------------------------",
        "-----------------------Encrypted Storage System Documentation----------------------",
        "=" * 83 + "\n"
    ]

    for i, line in enumerate(title_lines):
        center_text(stdscr, line, i)
    
    stdscr.refresh()




def warning(stdscr):
    stdscr.clear()
    docTitle(stdscr)
    center_text(stdscr,"Security Warning\n",5)

    warning_lines = [
        "Upon encryption, the system will display a password on the screen.\n",
        "The password is not stored anywhere, so it is the user's responsibility to save it.\n",
        "If the user loses the password, all encrypted content (PDF, photos, videos) will be permanently inaccessible.\n"
    ]
    center_text(stdscr,"[E]xit",13)

    for i, line in enumerate(warning_lines, start=7):
        center_text(stdscr, line, i)

    stdscr.refresh()

    while True:
        key = stdscr.getkey().upper()
        if key == "E":
            break 



def usage(stdscr):
    stdscr.clear()
    docTitle(stdscr)
    center_text(stdscr, "Usage Flow", 5)

    steps = [
        "1-The user adds information to the list or dictionary.",
        "2-The system encrypts and embeds the data into an invisible PDF file.",
        "3-If required, the user can also encrypt photos and videos.",
        "4-A unique encryption password is displayed to the user.",
        "5-The user must store this password safely, as recovery is impossible."
    ]
    center_text(stdscr,"[E]xit",15)

    for i, step in enumerate(steps, start=7):
        center_text(stdscr, step, i)

    stdscr.refresh()

    while True:
        key = stdscr.getkey().upper()
        if key == "E":
            break 



def documentation(stdscr):
    stdscr.clear()
    docTitle(stdscr)
    center_text(stdscr,"Overview\n",5)


    doc_lines = [
        "The Encrypted Storage System is designed to securely store user information in two formats:\n\n",
        "1. List Storage: A simple list where users can save information without any description.\n\n",
        "2. Dictionary Storage: A structured storage where users can save information along with descriptions.\n\n",
        "After adding all necessary information to either the list or dictionary, the system encrypts both\n",
        "and stores them inside an invisible PDF file.\n",
        "Additionally, the system provides functionality to encrypt photos and videos securely.\n"
    ]
    center_text(stdscr,"[E]xit [W]arning [U]sage",16)

    for i, line in enumerate(doc_lines, start=7):
        center_text(stdscr, line, i)

    stdscr.refresh()

    while True:
        key = stdscr.getkey().upper()
        if key == "E":
            break  
        elif key == "W":
            warning(stdscr)
        elif key == "U":
            usage(stdscr)


