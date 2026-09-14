from pathlib import Path
import pandas as pd

def ler_planilha(caminho):
    arquivo = Path(caminho)
    if not arquivo.is_file():
        raise FileNotFoundError(f"O arquivo {caminho} não foi encontrado.")
    
    dados = pd.read_excel(
        arquivo,
    dtype={"SKU": "string"}
    )

    if "SKU" not in dados.columns:
        raise ValueError("A coluna 'SKU' não foi encontrada na planilha.")
    dados ["SKU"] = dados["SKU"].str.strip()

    return dados

# função de exportação da planilha
def salvar_planilha(dados, caminho_saida):
    arquivo_saida = Path(caminho_saida)

    dados.to_excel(
        arquivo_saida,
        index=False,
    )

    return arquivo_saida