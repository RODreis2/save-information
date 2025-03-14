from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

def encrypt_file(file_path, output_path, key):
    # Gerar um vetor de inicialização (IV)
    iv = urandom(16)
    
    # Abrir o arquivo para leitura
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # Criar o objeto de cifra
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Criptografar os dados
    encrypted_data = encryptor.update(file_data) + encryptor.finalize()

    # Escrever o arquivo criptografado
    with open(output_path, 'wb') as f:
        f.write(iv + encrypted_data)  # Salvar o IV no início do arquivo criptografado

