from pathlib import Path

#extrai o código base do SKU, que é a parte antes do primeiro hífen
def extrair_codigo_base(sku):
    return sku.split("-")[0].strip()

#  Gera o nome do arquivo de imagem correspondente ao SKU, que é o código base seguido de ".jpg"
def gerar_nome_winthor(sku):
    codigo_base = extrair_codigo_base(sku)
    return f"{codigo_base}.jpg"

# Verifica se a imagem correspondente ao SKU existe na pasta especificada
def imagem_existe(pasta, nome_arquivo):
    caminho = Path(pasta) / nome_arquivo
    return caminho.is_file()

# verifica se a imagem correspondente ao SKU existe na pasta "WINTHOR" dentro da pasta de fotos especificada
def verificar_imagem_winthor(pasta_fotos, sku):
    nome_arquivo = gerar_nome_winthor(sku)
    pasta_winthor = Path(pasta_fotos) / "WINTHOR"
    return imagem_existe(pasta_winthor, nome_arquivo)