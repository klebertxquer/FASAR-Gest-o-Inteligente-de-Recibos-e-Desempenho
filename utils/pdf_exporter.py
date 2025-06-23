# utils/pdf_exporter.py

import io
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def exportar_pdf_simples(caminho_saida, titulo, dados):
    """Exporta dados como PDF simples com canvas."""
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

def gerar_pdf_vendas(dados, colunas):
    """Gera buffer PDF com os dados filtrados."""
    buffer = io.BytesIO()
    pdf = SimpleDocTemplate(buffer)

    tabela = [colunas] + [[str(linha.get(col, '')) for col in colunas] for linha in dados]
    elementos = [Table(tabela)]

    pdf.build(elementos)
    buffer.seek(0)
    return buffer



