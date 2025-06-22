# 📊 FASAR – Gestão Inteligente de Recibos e Desempenho

Sistema robusto em **Python + Flask** para leitura automática de comprovantes bancários (OCR em PDF/JPEG), análise de planilhas Excel e controle financeiro de empresas, vendedores e parceiros.

---

## 🔧 Funcionalidades Atuais

### ✅ 1. Leitor de Comprovantes (PDF/JPEG)
- Upload de até 10 arquivos de uma vez
- Extração automática de:
  - Valor
  - Data da transferência
  - Nome/CNPJ do Pagador
  - Nome/CNPJ do Recebedor
  - Banco de origem
  - ID da Transação
- Resultado exibido em tabela e armazenado localmente

### 📊 2. Análise de Excel (em desenvolvimento)
- Upload de planilhas com dados de vendas
- Filtro por vendedores
- Exportação em PDF da primeira aba

### 🏢 3. Cadastro de entidades (em desenvolvimento)
- Empresas, clientes, vendedores e parceiros
- Dados bancários com chave Pix

---

## 📁 Estrutura do Projeto

```
FASAR-Gestao-Inteligente-de-Recibos-e-Desempenho/
├── app.py                  # App principal Flask
├── requirements.txt       # Dependências
├── README.md              # Este arquivo
├── static/                # CSS, JS e uploads
│   ├── css/style.css
│   ├── js/scripts.js
│   └── uploads/
├── templates/             # HTMLs com layout e páginas
│   ├── layout.html
│   ├── dashboard.html
│   ├── leitor.html
│   ├── excel.html
│   └── cadastro.html
├── utils/                 # Scripts utilitários
│   ├── ocr_reader.py
│   ├── excel_analyzer.py
│   └── pdf_exporter.py
└── data/
    └── banco.db           # Banco SQLite local
```

---

## 🚀 Como executar localmente

### 1. Clone o repositório:
```bash
git clone https://github.com/klebertxquer/FASAR-Gest-o-Inteligente-de-Recibos-e-Desempenho.git
cd FASAR-Gest-o-Inteligente-de-Recibos-e-Desempenho
```

### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 3. Execute o sistema:
```bash
python app.py
```

Acesse no navegador: `http://127.0.0.1:5000`

---

## 🧠 Tecnologias Utilizadas
- Python 3.12+
- Flask
- pytesseract (OCR)
- pdfplumber (PDF)
- pandas + openpyxl (Excel)
- SQLAlchemy (Banco)
- reportlab (Exportação em PDF)
- Bootstrap/Tailwind (CSS opcional)

---

## 📦 Roadmap
- [x] OCR + leitura de comprovantes PDF/JPEG
- [ ] Análise Excel por vendedor
- [ ] Cadastro com relações entre empresas, clientes e parceiros
- [ ] Geração de relatórios mensais e gráficos
- [ ] Versão PWA para acesso mobile offline

---

## 🔐 Licença
Este projeto é de uso interno da FASAR Holding. Para parcerias ou versões comerciais, entre em contato.

---

**Desenvolvido com ❤️ por [klebertxquer](https://github.com/klebertxquer)**

