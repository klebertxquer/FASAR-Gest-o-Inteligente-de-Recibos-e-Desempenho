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


