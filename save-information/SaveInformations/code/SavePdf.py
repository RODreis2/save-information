from reportlab.pdfgen import canvas
import os

def save_to_pdf(filename, lista, dicionario):
    """Cria um PDF e salva uma lista e um dicionário nele."""
    c = canvas.Canvas(filename)

    # Salvando a lista no PDF
    c.drawString(100, 750, "Lista:")
    y = 730  # Posição Y inicial para escrever os itens da lista
    for item in lista:
        c.drawString(120, y, f"- {item}")
        y -= 20

    # Salvando o dicionário no PDF
    c.drawString(100, y-20, "Dicionário:")
    y -= 40
    for chave, valor in dicionario.items():
        c.drawString(120, y, f"{chave}: {valor}")
        y -= 20

    c.save()
    print(f"Arquivo salvo como: {filename}")


pegadinha = ["sim","nao"]
dicionariodomeme = {"isso kkkk": 123}
save_to_pdf("issoaimesmo",pegadinha, dicionariodomeme)