from Logics.Display import get_input
import curses
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

def encrypt_file(stdscr):
    stdscr.clear()

    # Display instructions
    stdscr.addstr(0, 0, "Example: provide the file path like '/home/you/want/encrypt/putin.jpg'")
    stdscr.refresh()

    # Get file path input
    file_path = get_input(stdscr, "Enter the file path to encrypt:", 2)
    stdscr.refresh()

    # Display the entered path for verification
    stdscr.addstr(5, 2, f"Entered path: {file_path}", curses.A_BOLD)
    stdscr.refresh()

    # Check if the file exists
    try:
        with open(file_path, 'rb') as f:
            stdscr.addstr(7, 2, "File found!", curses.A_BOLD)
    except FileNotFoundError:
        stdscr.addstr(7, 2, "File not found. Please check the path.", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()  # Wait for user input before exiting
        return

    # Get output file name
    output_path = get_input(stdscr, "Enter the new name for the encrypted file:", 8)
    stdscr.refresh()

    # Generate encryption key
    key = urandom(32)

    # Save the key to a file
    key_path = output_path + ".key"
    with open(key_path, "wb") as key_file:
        key_file.write(key)

    # Display the encryption key
    stdscr.clear()
    stdscr.addstr(1, 2, "This is your key to DECRYPT the file. DO NOT FORGET!", curses.A_BOLD)
    stdscr.addstr(2, 2, key.hex(), curses.A_UNDERLINE)  # Display the key in hexadecimal
    stdscr.addstr(4, 2, f"Key saved at: {key_path}", curses.A_BOLD)
    stdscr.refresh()

    curses.noecho()  # Disable terminal echo for security

    try:
        # Generate the IV
        iv = urandom(16)

        # Read file data
        with open(file_path, 'rb') as f:
            file_data = f.read()

        # Create cipher object
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Encrypt the data
        encrypted_data = encryptor.update(file_data) + encryptor.finalize()

        # Write the encrypted file
        with open(output_path, 'wb') as f:
            f.write(iv + encrypted_data)

        stdscr.addstr(10, 2, "Encryption successful!", curses.A_BOLD)
    except Exception as e:
        stdscr.addstr(10, 2, f"Error: {str(e)}", curses.color_pair(1))

    stdscr.refresh()
    stdscr.getch()  # Wait for user input before exiting

if __name__ == "__main__":
    curses.wrapper(encrypt_file)