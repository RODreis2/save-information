import pdfplumber
import os

def load_from_pdf(filename):
    lista = []
    dicionario = {}

    if not os.path.exists(filename):
        print("Arquivo não encontrado! Criando um novo.")
        return lista, dicionario  # Retorna listas vazias se o arquivo não existir

    with pdfplumber.open(filename) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

    lines = text.split("\n")  # Divide o conteúdo do PDF em linhas

    i = 0
    while i < len(lines):
        if lines[i] == "List:":
            i += 1
            while i < len(lines) and not lines[i].startswith("Dict:"):
                lista.append(lines[i].replace("- ", ""))  # Remove o marcador da lista
                i += 1
        if lines[i] == "Dict:":
            i += 1
            while i < len(lines):
                key_value = lines[i].split(": ")
                if len(key_value) == 2:
                    chave, valor = key_value
                    dicionario[chave] = valor if not valor.isdigit() else int(valor)  # Converte para inteiro se for número
                i += 1
        i += 1

    print(lista, dicionario)
    return lista, dicionario
    

