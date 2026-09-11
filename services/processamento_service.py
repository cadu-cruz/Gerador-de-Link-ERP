from services.link_service import *
from services.status_service import gerar_status
import pandas as pd

def processar_sku(pasta_fotos, sku):
    links = {
    "WINTHOR": link_imagem_winthor(pasta_fotos, sku),
    "VTEX": link_imagem_vtex(pasta_fotos, sku),
    "ML": link_imagem_ml(pasta_fotos, sku)
    }

    for numero_img in range(2, 9):
        nome_pasta = f"IMG_{numero_img}"
        links[nome_pasta] = link_imagem_img(pasta_fotos,sku,numero_img,)

    status = gerar_status(links)

    resultado = {"SKU": sku}
    resultado.update(links)
    resultado["STATUS"] = status

    return resultado

def processar_dados(dados, pasta_fotos):
    resultados = []

    for sku in dados["SKU"]:
        if pd.isna(sku) or not str(sku).strip():
            continue

        sku_limpo = str(sku).strip()
        resultado_sku = processar_sku(pasta_fotos, sku_limpo)
        resultados.append(resultado_sku)
        
    return pd.DataFrame(resultados)
