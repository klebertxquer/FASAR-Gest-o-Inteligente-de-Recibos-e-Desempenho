from flask import Flask, render_template, request, send_file
import os
import io
import pandas as pd
from utils.ocr_reader import extrair_texto_de_pdf, extrair_texto_de_imagem, extrair_dados
from utils.db_models import session, Entidade
from utils.pdf_exporter import gerar_pdf_vendas
from utils.excel_analyzer import ler_planilha
from reportlab.platypus import SimpleDocTemplate, Table

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template("dashboard.html")

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

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nova = Entidade(
            tipo=request.form['tipo'],
            nome=request.form['nome'],
            documento=request.form['documento'],
            banco=request.form['banco'],
            agencia=request.form['agencia'],
            conta=request.form['conta'],
            pix=request.form['pix']
        )
        session.add(nova)
        session.commit()
    registros = session.query(Entidade).all()
    return render_template("cadastro.html", registros=registros)

if __name__ == '__main__':
    app.run(debug=True)
