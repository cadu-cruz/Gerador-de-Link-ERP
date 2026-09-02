from services.imagem_service import *
from services.link_service import *

print(extrair_codigo_base("ABC123-S01"))

assert gerar_nome_winthor("ABC123-S01") == "ABC123.jpg"
assert gerar_nome_winthor("ABC123-M01") == "ABC123.jpg"
print("All tests passed!")

print(imagem_existe("FOTOS/WINTHOR", "ABC123.jpg"))
print(imagem_existe("FOTOS/WINTHOR", "NAO_EXISTE.jpg"))

assert verificar_imagem_winthor("FOTOS", "ABC123-S01") == True
assert verificar_imagem_winthor("FOTOS", "NAO_EXISTE-S01") == False
print ("Verificação do Winthor funcionando corretamente!")

assert link_imagem_winthor("FOTOS", "ABC123-S01") == "https://retaguarda.benimports.com.br/WINTHOR/ABC123.jpg"
print("Link do Winthor funcionando corretamente!")

assert link_imagem_winthor("FOTOS", "NAO_EXISTE-S01") == ""
print("Link do Winthor para imagem não existente funcionando corretamente!")