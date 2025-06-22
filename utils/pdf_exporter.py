from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def exportar_pdf(caminho_saida, titulo, dados):
    c = canvas.Canvas(caminho_saida, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(50, 800, titulo)

    y = 760
    for linha in dados:
        texto = ' | '.join([str(item) for item in linha])
        c.drawString(50, y, texto)
        y -= 20
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 800

    c.save()

