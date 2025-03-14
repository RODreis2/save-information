import curses

def menu(stdscr):
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

    # Hide cursor
    curses.curs_set(0)

    # Clear screen
    stdscr.clear()

    # Get screen size
    height, width = stdscr.getmaxyx()

    # Box dimensions
    box_width = 50
    box_height = 20

    # Ensure the terminal is large enough
    if height < box_height + 2 or width < box_width + 2:
        stdscr.addstr(0, 0, "Terminal too small. Resize and try again.", curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()
        return

    # Center position
    start_y = (height - box_height) // 2
    start_x = (width - box_width) // 2

    # Draw the box with proper borders
    for y in range(start_y, start_y + box_height):
        for x in range(start_x, start_x + box_width):
            if y == start_y or y == start_y + box_height - 1:  # Top & Bottom
                stdscr.addch(y, x, curses.ACS_HLINE)
            elif x == start_x or x == start_x + box_width - 1:  # Sides
                stdscr.addch(y, x, curses.ACS_VLINE)

    # Draw corners
    stdscr.addch(start_y, start_x, curses.ACS_ULCORNER)  # Upper-left
    stdscr.addch(start_y, start_x + box_width - 1, curses.ACS_URCORNER)  # Upper-right
    stdscr.addch(start_y + box_height - 1, start_x, curses.ACS_LLCORNER)  # Lower-left
    stdscr.addch(start_y + box_height - 1, start_x + box_width - 1, curses.ACS_LRCORNER)  # Lower-right

    # Add text inside the box
    stdscr.addstr(start_y + 2, start_x + 2, "This is a box with proper borders!", curses.color_pair(1))

    # Display header message
    header = "=" * 83
    stdscr.addstr(0, max(0, (width - len(header)) // 2), header)
    stdscr.addstr(1, max(0, (width - len(header)) // 2), "This application uses a list and a dictionary where you can add values.")
    stdscr.addstr(2, max(0, (width - len(header)) // 2), header)

    # Show exit message
    stdscr.addstr(0, 2, "Press any key to exit...", curses.A_BOLD)
    
    # Refresh and wait for user input
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(menu)

