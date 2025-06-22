import pandas as pd

def carregar_excel(caminho):
    df = pd.read_excel(caminho)
    return df

def filtrar_por_vendedor(df, nome_vendedor):
    return df[df['Vendedor'].str.contains(nome_vendedor, case=False, na=False)]

