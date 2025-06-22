from flask import Flask, render_template, request
import os
from utils.ocr_reader import extrair_texto_de_pdf, extrair_texto_de_imagem, extrair_dados

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Página inicial
@app.route('/')
def home():
    return render_template("dashboard.html")

# Página de upload e leitura de comprovantes
@app.route('/leitor', methods=['GET', 'POST'])
def leitor():
    resultados = []
    if request.method == 'POST':
        arquivos = request.files.getlist('files')
        for arquivo in arquivos:
            if arquivo.filename == '':
                continue

            caminho = os.path.join(app.config['UPLOAD_FOLDER'], arquivo.filename)
            arquivo.save(caminho)

            if arquivo.filename.lower().endswith('.pdf'):
                texto = extrair_texto_de_pdf(caminho)
            elif arquivo.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                texto = extrair_texto_de_imagem(caminho)
            else:
                texto = ""

            dados_extraidos = extrair_dados(texto)
            resultados.append(dados_extraidos)

    return render_template("leitor.html", resultados=resultados)

# Página de análise Excel (a ser implementada)
@app.route('/excel')
def excel():
    return render_template("excel.html")

# Página de cadastro (a ser implementada)
@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")

if __name__ == '__main__':
    app.run(debug=True)

from utils.excel_analyzer import ler_planilha
import pandas as pd
from flask import send_file
import io
from reportlab.platypus import SimpleDocTemplate, Table

@app.route('/excel', methods=['GET', 'POST'])
def excel():
    dados = []
    colunas = []
    nome_arquivo = ''
    if request.method == 'POST':
        arquivo = request.files['arquivo_excel']
        if arquivo:
            nome_arquivo = arquivo.filename
            caminho = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
            arquivo.save(caminho)
            dados, colunas = ler_planilha(caminho)
    return render_template("excel.html", dados=dados, colunas=colunas, nome_arquivo=nome_arquivo)

@app.route('/exportar_pdf', methods=['POST'])
def exportar_pdf():
    nome_arquivo = request.form['arquivo_excel']
    vendedor_filtro = request.form['vendedor']
    caminho = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)

    dados, colunas = ler_planilha(caminho)
    filtrado = [linha for linha in dados if str(linha.get('Vendedor', '')) == vendedor_filtro]

    buffer = io.BytesIO()
    pdf = SimpleDocTemplate(buffer)
    tabela = [colunas] + [[linha[col] for col in colunas] for linha in filtrado]
    elementos = [Table(tabela)]
    pdf.build(elementos)
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="relatorio_vendas.pdf", mimetype='application/pdf')

    from utils.pdf_exporter import gerar_pdf_vendas
