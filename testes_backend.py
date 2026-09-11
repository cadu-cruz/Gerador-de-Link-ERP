from services.imagem_service import *
from services.link_service import *
from services.status_service import gerar_status

#testando extrair ABC123 de ABC123-S01
print(extrair_codigo_base("ABC123-S01"))

#testando adicionar .jpg ao final do código base
print(gerar_nome_codigo_base("ABC123-S01"))

#testando se a imagem existe na pasta especificada
print(imagem_existe("FOTOS/WINTHOR", "ABC123.jpg"))
print(imagem_existe("FOTOS/WINTHOR", "NAO_EXISTE.jpg"))
print(imagem_existe("FOTOS/VTEX", "ABC123-S01_1.jpg"))
print(imagem_existe("FOTOS/VTEX", "NAO_EXISTE-S01_1.jpg"))

#testando se a imagem existe na pasta WINTHOR
assert verificar_imagem_winthor("FOTOS", "ABC123-S01") == True
assert verificar_imagem_winthor("FOTOS", "NAO_EXISTE-S01") == False
print ("Verificação do Winthor funcionando corretamente!")

#testando gerar nome vtex e ml
assert gerar_nome_vtex_ml("ABC123-S01") == "ABC123-S01_1.jpg"
assert gerar_nome_vtex_ml("ABC123-M01") == "ABC123-M01_1.jpg"

#testando criar o link da imagem da pasta winthor
assert link_imagem_winthor("FOTOS", "ABC123-S01") == "https://retaguarda.benimports.com.br/WINTHOR/ABC123.jpg"
print("Link do Winthor funcionando corretamente!")

assert link_imagem_winthor("FOTOS", "NAO_EXISTE-S01") == ""
print("Link do Winthor para imagem não existente funcionando corretamente!")

#testando se a imagem existe na pasta VTEX e criando o link
assert link_imagem_vtex("FOTOS", "ABC123-S01") == "https://retaguarda.benimports.com.br/VTEX/ABC123-S01_1.jpg"
print("Link do VTEX funcionando corretamente!")

assert link_imagem_vtex("FOTOS", "NAO_EXISTE-S01") == ""
print("Link do VTEX para imagem não existente funcionando corretamente!")

#testando se a imagem existe na pasta ML e criando o link
assert link_imagem_ml("FOTOS", "ABC123-M01") == "https://retaguarda.benimports.com.br/ML/ABC123-M01_1.jpg"
print("Link do ML funcionando corretamente!")

assert link_imagem_ml("FOTOS", "NAO_EXISTE-M01") == ""
print("Link do ML para imagem não existente funcionando corretamente!")

#testando se a imagem existe na pasta determinada entre IMG_2 e IMG_8 e criando o link e fazendo tratamento de erro de pasta que nao existe.
try:
    link_imagem_img("FOTOS", "ABC123-S01", 9)

except ValueError as erro:
    assert str(erro) == (
        "Número da pasta IMG inválido. Deve ser entre 2 e 8."
    )
    print("Tratamento de erro da pasta IMG funcionando!")

else:
    raise AssertionError(
        "Esperava-se um ValueError, mas nenhum foi levantado."
    )

assert link_imagem_img("FOTOS", "ABC123-S01", 2) == "https://retaguarda.benimports.com.br/IMG_2/ABC123.jpg"
print("Link da pasta IMG_2 funcionando corretamente!")


#Testando a função gerar_status com links completos e incompletos
links_completos = {
    "WINTHOR": "link",
    "VTEX": "link",
    "ML": "link",
    "IMG_2": "link",
}

links_incompletos = {
    "WINTHOR": "",
    "VTEX": "",
    "ML": "",
    "IMG_2": "",
}

assert (gerar_status(links_completos)) == "OK"
assert (gerar_status(links_incompletos)) == "Faltando links para as pastas: WINTHOR, VTEX, ML, IMG_2"

print("Função gerar_status funcionando corretamente com links completos e incompletos!")