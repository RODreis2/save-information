from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


def decrypt_file(file_path, output_path, key):
    # Abrir o arquivo criptografado
    with open(file_path, 'rb') as f:
        iv = f.read(16)  # O IV é os primeiros 16 bytes do arquivo
        encrypted_data = f.read()

    # Criar o objeto de cifra
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Descriptografar os dados
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Salvar os dados descriptografados no arquivo de saída
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

