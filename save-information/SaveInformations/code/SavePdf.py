import curses
from reportlab.pdfgen import canvas
import os

def save_to_pdf(stdscr, filename, ListToPdf, DictToPdf):
    stdscr.clear()
    stdscr.addstr(0, 0, "Creating PDF...")
    stdscr.refresh()
    
    c = canvas.Canvas(filename)
    
    # Saving list to PDF
    c.drawString(100, 750, "List:")
    y = 730
    for item in ListToPdf:
        c.drawString(120, y, f"- {item}")
        y -= 20
    
    c.drawString(100, y - 20, "Dict:")
    y -= 40
    for key, value in DictToPdf.items():
        c.drawString(120, y, f"{key}: {value}")
        y -= 20
    
    c.save()
    
    # Hide the file
    if os.name == "nt":
        os.system(f"attrib +h {filename}.pdf")
    elif os.name == "posix":
        hidden_filename = f".{filename}.pdf"
        os.rename(filename, hidden_filename)
        filename = hidden_filename
    
    stdscr.addstr(2, 0, f"File saved as hidden: {filename}")
    stdscr.addstr(4, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(save_to_pdf)
