from pathlib import Path

#extrai o código base do SKU, que é a parte antes do primeiro hífen
def extrair_codigo_base(sku):
    return sku.split("-")[0].strip()

#  Gera o nome do arquivo de imagem correspondente ao SKU, que é o código base seguido de ".jpg"
def gerar_nome_codigo_base(sku):
    codigo_base = extrair_codigo_base(sku)
    return f"{codigo_base}.jpg"

# Verifica se a imagem correspondente ao SKU existe na pasta especificada
def imagem_existe(pasta, nome_arquivo):
    caminho = Path(pasta) / nome_arquivo
    return caminho.is_file()

# verifica se a imagem correspondente ao SKU existe na pasta "WINTHOR" dentro da pasta de fotos especificada
def verificar_imagem_winthor(pasta_fotos, sku):
    nome_arquivo = gerar_nome_codigo_base(sku)
    pasta_winthor = Path(pasta_fotos) / "WINTHOR"
    return imagem_existe(pasta_winthor, nome_arquivo)

# Gera o nome do arquivo de imagem correspondente ao SKU para a plataforma VTEX, que é o SKU seguido de "_1.jpg"
def gerar_nome_vtex_ml(sku):
    codigo_base = sku + "_1.jpg"
    return codigo_base

# verifica se a imagem correspondente ao SKU existe na pasta "VTEX" dentro da pasta de fotos especificada
def verificar_imagem_vtex(pasta_fotos, sku):
    nome_arquivo = gerar_nome_vtex_ml(sku)
    pasta_vtex = Path(pasta_fotos) / "VTEX"
    return imagem_existe(pasta_vtex, nome_arquivo)

# verifica se a imagem correspondente ao SKU existe na pasta "ML" dentro da pasta de fotos especificada
def verificar_imagem_ml(pasta_fotos, sku):
    nome_arquivo = gerar_nome_vtex_ml(sku)
    pasta_ml = Path(pasta_fotos) / "ML"
    return imagem_existe(pasta_ml, nome_arquivo)

# verificar todas as pastas IMG
def verificar_imagem_img(pasta_fotos, sku, numero_img):
    if numero_img not in range(2, 9):
            raise ValueError("Número da pasta IMG inválido. Deve ser entre 2 e 8.")
    nome_arquivo = gerar_nome_codigo_base(sku)
    pasta = f"IMG_{numero_img}"
    pasta_fotos = Path(pasta_fotos) / pasta
    return imagem_existe(pasta_fotos, nome_arquivo)
