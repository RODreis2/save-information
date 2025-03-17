def get_input(stdscr, prompt, row=0, col=0):
    """Captura a entrada do usuário e exibe em tempo real com suporte ao backspace."""
    stdscr.addstr(row, col, prompt)
    stdscr.refresh()

    input_str = ""
    while True:
        # Move o cursor para a linha abaixo do prompt, sem reposicionar o texto "You are typing: "
        stdscr.move(row + 1, col)
        stdscr.clrtoeol()  # Limpa a linha atual a partir da posição do cursor

        # Exibe a mensagem de digitação
        stdscr.addstr("You are typing: " + input_str)
        stdscr.refresh()

        key = stdscr.getch()  # Captura a tecla pressionada

        # Se pressionar ENTER (código 10), sai do loop
        if key == 10:
            break
        elif key == 27:  # Se pressionar ESC (código 27), sai do loop
            return None
        elif key == 263:  # Se pressionar BACKSPACE (código 263), remove o último caractere
            input_str = input_str[:-1]
        elif key >= 32 and key <= 126:  # Verifica se a tecla pressionada é um caractere imprimível
            input_str += chr(key)  # Adiciona o caractere digitado à string

    return input_str  # Retorna a string final digitada

       

