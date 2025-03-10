from reportlab.pdfgen import canvas
import os

def save_to_pdf(filename, ListToPdf, DictToPdf):
    """Cria um PDF e salva uma lista e um dicionário nele."""
    c = canvas.Canvas(filename)

    # Salvando a lista no PDF
    c.drawString(100, 750, "List:")
    y = 730  # Posição Y inicial para escrever os itens da lista
    for item in ListToPdf:
        c.drawString(120, y, f"- {item}")
        y -= 20

    c.drawString(100, y-20, "Dict:")
    y -= 40
    for chave, valor in DictToPdf.items():
        c.drawString(120, y, f"{chave}: {valor}")
        y -= 20

    c.save()
    print(f"File save by name: {filename}")


liust = [1, 2, 3]
liust2 = {1:"isso"}
save_to_pdf("pdf.pdf", liust,liust2)