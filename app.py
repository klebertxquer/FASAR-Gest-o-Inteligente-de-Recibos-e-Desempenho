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

