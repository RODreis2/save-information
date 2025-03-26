from Logics.Display import get_input
import curses
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def decrypt_file(stdscr):
    stdscr.clear()

    # Display instructions
    stdscr.addstr(0, 2, "Example: pass the encrypted file path like 'you/encrypted.jpg'")
    stdscr.refresh()

    # Get encrypted file path input using get_input()
    file_path = get_input(stdscr, "Enter the encrypted file path:", 2)
    stdscr.refresh()

    # Check if the file path is empty
    if not file_path:
        stdscr.addstr(5, 2, "Error: File path cannot be empty.", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()  # Wait for user input before exiting
        return  # Exit the function

    # Check if the file exists
    if not os.path.exists(file_path):
        stdscr.addstr(5, 2, "Error: File does not exist.", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()  # Wait for user input before exiting
        return  # Exit the function

    # Get output file name
    stdscr.addstr(5, 2, "Example: 'decrypted_output.jpg'")
    output_path = get_input(stdscr, "Write the new name for the decrypted file:", 6)
    stdscr.refresh()

    # Check if output path is empty
    if not output_path:
        stdscr.addstr(7, 2, "Error: Output path cannot be empty.", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()  # Wait for user input before exiting
        return  # Exit the function

    # Get decryption key from user
    stdscr.addstr(9, 2, "Enter the 64-character decryption key:")
    stdscr.refresh()

    key_input = get_input(stdscr, "Enter the key:", 10)
    
    # Check if the key is valid
    if len(key_input) != 64:
        stdscr.addstr(11, 2, "Error: Key must be 64 characters.", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()  # Wait for user input before exiting
        return  # Exit the function

    try:
        # Convert key from hex back to bytes
        key = bytes.fromhex(key_input)

        # Read the encrypted file
        with open(file_path, 'rb') as f:
            iv = f.read(16)  # First 16 bytes are the IV
            encrypted_data = f.read()

        # Create cipher object
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Decrypt data
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

        # Write decrypted file
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)

        stdscr.addstr(12, 2, "Decryption successful!", curses.A_BOLD)
    except Exception as e:
        stdscr.addstr(12, 2, f"Error: {str(e)}", curses.color_pair(1))

    stdscr.refresh()
    stdscr.getch()  # Wait for user input before exiting

if __name__ == "__main__":
    curses.wrapper(decrypt_file)
