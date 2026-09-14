from services.link_service import *
from services.status_service import gerar_status
import pandas as pd

def identificar_plataforma(sku):
    #identifica se o SKU é do site(VTEX) ou do marketplace(ML)
    if "-" not in sku: 
        return "WINTHOR"
    
    sufixo = sku.rsplit("-", 1)[1].upper()

    if sufixo.startswith("S"):
        return "VTEX"

    if sufixo.startswith("M"):
        return "ML"

def processar_sku(pasta_fotos, sku):
    #processa o link do arquivo para cada SKU
    imagem_produto_1 = identificar_plataforma(sku)

    if imagem_produto_1 == "VTEX":
        imagem_produto_1 = link_imagem_vtex(pasta_fotos, sku)

    if imagem_produto_1 == "WINTHOR":
        imagem_produto_1 = link_imagem_winthor(pasta_fotos, sku)

    if imagem_produto_1 == "ML":
        imagem_produto_1 = link_imagem_ml(pasta_fotos, sku)  

    links = {
    "IMG_1": imagem_produto_1,
    }

    for numero_img in range(2, 10):
        nome_pasta = f"IMG_{numero_img}"
        links[nome_pasta] = link_imagem_img(pasta_fotos,sku,numero_img,)

    status = gerar_status(links)

    resultado = {"SKU": sku}
    resultado.update(links)
    resultado["STATUS"] = status

    return resultado

def processar_dados(dados, pasta_fotos):
    #Gera a planilha final com os nomes das colunas corretos
    resultados = []

    for sku in dados["SKU"]:
        if pd.isna(sku) or not str(sku).strip():
            continue

        sku_limpo = str(sku).strip()
        resultado_sku = processar_sku(pasta_fotos, sku_limpo)
        resultados.append(resultado_sku)
        resultado_final = pd.DataFrame(resultados)
        mapa_colunas = {
            "IMG_1": "IMAGEM_PRODUTO_1",
            "IMG_2": "IMAGEM_PRODUTO_2",
            "IMG_3": "IMAGEM_PRODUTO_3",
            "IMG_4": "IMAGEM_PRODUTO_4",
            "IMG_5": "IMAGEM_PRODUTO_5",
            "IMG_6": "IMAGEM_PRODUTO_6",
            "IMG_7": "IMAGEM_PRODUTO_7",
            "IMG_8": "IMAGEM_PRODUTO_8",
            "IMG_9": "IMAGEM_PRODUTO_9"

        }

        resultado_final = resultado_final.rename(columns=mapa_colunas)      

    return resultado_final
