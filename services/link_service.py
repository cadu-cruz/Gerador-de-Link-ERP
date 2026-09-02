from services.imagem_service import (
    verificar_imagem_winthor,
    gerar_nome_winthor,
)

def link_imagem_winthor(pasta_fotos, sku):
    if verificar_imagem_winthor(pasta_fotos, sku):
        nome_arquivo = gerar_nome_winthor(sku)
        return f"https://retaguarda.benimports.com.br/WINTHOR/{nome_arquivo}"
    return ""
