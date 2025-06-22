import pytesseract
import pdfplumber
from PIL import Image
import re
import os

def extrair_texto_de_pdf(caminho_pdf):
    texto_total = ""
    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            texto_total += pagina.extract_text() + "\n"
    return texto_total

def extrair_texto_de_imagem(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    texto = pytesseract.image_to_string(imagem, lang='por')
    return texto

def extrair_dados(texto):
    # Expressões regulares simples
    valor = re.search(r'R\$ ?[\d\.,]+', texto)
    data = re.search(r'\d{2}/\d{2}/\d{4}', texto)
    pagador = re.search(r'(Pagador|Devedor|Emitente|Remetente).*?: *(.*)', texto, re.IGNORECASE)
    recebedor = re.search(r'(Destinatário|Recebedor|Favorecido|Credor).*?: *(.*)', texto, re.IGNORECASE)
    cpf_cnpj = re.findall(r'\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}', texto)
    banco = re.search(r'(Banco|Instituição|Caixa Econômica|Bradesco|Santander|Itaú)', texto, re.IGNORECASE)
    id_tx = re.search(r'\b[A-Z0-9]{20,}\b', texto)

    return {
        'data': data.group() if data else '',
        'valor': valor.group() if valor else '',
        'pagador': pagador.group(2).strip() if pagador else '',
        'cpf_pagador': cpf_cnpj[0] if len(cpf_cnpj) > 0 else '',
        'recebedor': recebedor.group(2).strip() if recebedor else '',
        'cpf_recebedor': cpf_cnpj[1] if len(cpf_cnpj) > 1 else '',
        'banco': banco.group() if banco else '',
        'id_transacao': id_tx.group() if id_tx else ''
    }

