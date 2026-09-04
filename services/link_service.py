from services.imagem_service import (
    verificar_imagem_winthor,
    gerar_nome_codigo_base,
    verificar_imagem_vtex,
    gerar_nome_vtex_ml,
    verificar_imagem_ml,
    verificar_imagem_img
    )

def link_imagem_winthor(pasta_fotos, sku):
    if verificar_imagem_winthor(pasta_fotos, sku):
        nome_arquivo = gerar_nome_codigo_base(sku)
        return f"https://retaguarda.benimports.com.br/WINTHOR/{nome_arquivo}"
    return ""

def link_imagem_vtex(pasta_fotos, sku):
    if verificar_imagem_vtex(pasta_fotos, sku):
        nome_arquivo = gerar_nome_vtex_ml(sku)
        return f"https://retaguarda.benimports.com.br/VTEX/{nome_arquivo}"
    return ""

def link_imagem_ml(pasta_fotos, sku):
    if verificar_imagem_ml(pasta_fotos, sku):
        nome_arquivo = gerar_nome_vtex_ml(sku)
        return f"https://retaguarda.benimports.com.br/ML/{nome_arquivo}"
    return ""

def link_imagem_img(pasta_fotos, sku, numero_img):
    if verificar_imagem_img(pasta_fotos, sku, numero_img):
        nome_arquivo = gerar_nome_codigo_base(sku)
        pasta = f"IMG_{numero_img}"
        return f"https://retaguarda.benimports.com.br/{pasta}/{nome_arquivo}"
    return ""