# Gerador de Links ERP 

## Backend
- Python
- CustomTkinter
- Pandas

## Objetivo 
Criar uma aplicação local em Python utilizando Ctk para gerar automaticamente os links de arquivos de imagem a partir de uma planilha contendo os SKU's.

- O programa deverá verificar o código dos produtos na planilha e apartir disso verifiar quais imagens desse produto realmente existem nas pastas do computador e gerar uma nova planilha com os links das imagens pronta para utilização. 

# Fluxo do Programa 
1. Abrir a GUI.
2. Botão "Selecionar Planilha" para selecionar o arquivo Excel contendo os SKU's. 
3. Botão "Selecionar a pasta" para selecionar a pasta principal com as bubpastas com os arquivos de fotos."FOTOS". 
4. O backend lê todos os SKU's. 
5. Para cada código SKU: - verifica todas as pastas de imagens - gera os links apenas quando encontrar o arquivo 
6. Exporta uma nova planilha. 
7. Exibe resumo da execução. 

# Estrutura das Pastas FOTOS/ WINTHOR/ VTEX/ ML/ IMG_2/ IMG_3/ IMG_4/ IMG_5/ IMG_6/ IMG_7/ IMG_8/ 

# Entrada Planilha Excel. 
Exemplo: 
SKU 
ABC123-S01 
ABC123-S02 
ABC123-S03
ABC123-M01
ABC123-M02
ABC123-M03

# Regras de Geração 

## IMG_2 até IMG_8 Usar apenas a parte do SKU antes do "-". 
Exemplo SKU: ABC123-S01 

arquivo procurado: ABC123.jpg 

Link a ser gerado: https://retaguarda.benimports.com.br/IMG_2/ABC123_1.jpg 

## WINTHOR Mesmo comportamento das IMG. 
Arquivo procurado: ABC123.jpg 

Link a ser gerado: https://retaguarda.benimports.com.br/WINTHOR/ABC123.jpg 

## VTEX Usar SKU completo. 
Arquivo procurado: ABC123-S01_1.jpg 

Link a ser gerado: https://retaguarda.benimports.com.br/VTEX/ABC123-S01_1.jpg 

## ML Usar SKU Completo. 
Exemplo Arquivo esperado ABC123-M01_1.jpg 

Link a ser gerado: https://retaguarda.benimports.com.br/ML/ABC123-M01_1.jpg 

# Verificação Antes de gerar o link: Verificar se o arquivo existe. 
Se existir: gerar link. 
Se não existir: deixar célula vazia.

# Planilha de Saída 
SKU WINTHOR VTEX ML IMAGEM_PRODUTO_2 para a IMG_2 IMAGEM_PRODUTO_3 para a IMG_3 IMAGEM_PRODUTO_4 para a IMG_4 IMAGEM_PRODUTO_5 para a IMG_5 IMAGEM_PRODUTO_6 para a IMG_6 IMAGEM_PRODUTO_7 para a IMG_7 IMAGEM_PRODUTO_8 para a IMG_8 STATUS 

Exemplo SKU        WINTHOR   VTEX    ML    IMAGEM_PRODUTO_2... 
        ABC123-S01 link      link    link  link 

# STATUS 

Se todas as imagens forem encontradas: OK 

Se faltar qualquer imagem: 
NÃO ENCONTRADO (informar quais pastas faltaram) 

Exemplo 
Faltando: ML IMG_5 IMG_7 
Resultado: "Faltando: ML, IMG_5, IMG_7" --- 

# Interface 
Título Gerador de Links ERP 
Botão Selecionar Excel 
Botão Selecionar Pasta FOTOS 
Botão Gerar Links 
Botão para abrir a planilha de saída criada
Mensagem final. Exemplo: Processados: 500 produtos Tempo: 18 segundos