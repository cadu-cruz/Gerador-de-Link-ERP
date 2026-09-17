# Gerador de Links ERP

Automação local desenvolvida em python para geração dos links de imagens para os anuncios nas plataformas marketplaces que a empresa é ativa.

A automação lê os SKUs dos produtos informados na planilha, verifica quais imagens existem nas pastas do computador e exporta uma nova planilha com os links encontrados e o status de cada produto.

## Tecnologias utilizadas

- Python
- CustomTkinter
- Pandas
- OpenPyXL

## Funcionalidades

- Seleção de uma planilha Excel pela interface gráfica.
- Seleção da pasta principal que contém as imagens.
- Leitura e tratamento da coluna `SKU`.
- Verificação da existência das imagens antes da geração dos links.
- Identificação de plataforma devera ser gerado os links (Site ou Mercado Livre) pela estrutura do SKU.
- Geração das colunas `IMAGEM_PRODUTO_1` até `IMAGEM_PRODUTO_9` com os links encontrado.
- Geração de um status para imagens não encontradas.
- Exportação do resultado para uma nova planilha Excel.
- Log visual do processamento.
- Abertura da planilha gerada pela própria interface.

## Fluxo do sistema

1. O usuário inicia a aplicação.
2. Seleciona uma planilha Excel que contenha a coluna `SKU`.
3. Seleciona a pasta principal de fotos.
4. Clica em **Gerar links**.
5. O sistema lê e trata os SKUs da planilha.
6. Para cada SKU, verifica quais arquivos de imagem existem.
7. Os links são gerados somente para as imagens encontradas.
8. Após o processamento, o usuário escolhe onde salvar o resultado.
9. O sistema exporta a nova planilha e libera o botão **Abrir resultado**.

## Estrutura esperada da pasta de fotos

```text
FOTOS/
├── WINTHOR/
├── VTEX/
├── ML/
├── IMG_2/
├── IMG_3/
├── IMG_4/
├── IMG_5/
├── IMG_6/
├── IMG_7/
├── IMG_8/
└── IMG_9/
```

Ao selecionar as fotos na interface, o usuário deve escolher a pasta principal que contém essas subpastas.

## Formato da planilha de entrada

A planilha deve ser um arquivo `.xlsx` e possuir uma coluna com o título exato `SKU`.

Exemplo:

| SKU |
| --- |
| ABC123 |
| ABC123-S01 |
| ABC123-S02 |
| ABC123-M01 |
| ABC123-M02 |

Os espaços existentes antes ou depois dos SKUs são removidos durante a leitura.

## Regras de geração

### IMAGEM_PRODUTO_1

A origem da primeira imagem é definida pela estrutura do SKU.

#### WINTHOR

Um SKU sem hífen utiliza a pasta `WINTHOR`.

Exemplo:

```text
SKU: ABC123
Arquivo procurado: WINTHOR/ABC123.jpg
Link gerado: https://retaguarda.benimports.com.br/WINTHOR/ABC123.jpg
```

#### VTEX

Um SKU cujo sufixo começa com `S` utiliza a pasta `VTEX`. O arquivo deve possuir o SKU completo seguido de `_1.jpg`.

Exemplo:

```text
SKU: ABC123-S01
Arquivo procurado: VTEX/ABC123-S01_1.jpg
Link gerado: https://retaguarda.benimports.com.br/VTEX/ABC123-S01_1.jpg
```

Qualquer sufixo iniciado com `S` segue essa regra.

#### ML

Um SKU cujo sufixo começa com `M` utiliza a pasta `ML`. O arquivo deve possuir o SKU completo seguido de `_1.jpg`.

Exemplo:

```text
SKU: ABC123-M01
Arquivo procurado: ML/ABC123-M01_1.jpg
Link gerado: https://retaguarda.benimports.com.br/ML/ABC123-M01_1.jpg
```

### IMAGEM_PRODUTO_2 até IMAGEM_PRODUTO_9

Para as imagens adicionais, o sistema utiliza somente a parte do SKU anterior ao primeiro hífen.

Exemplo com o SKU `ABC123-S01`:

```text
Arquivo procurado na IMG_2: IMG_2/ABC123.jpg
Link gerado: https://retaguarda.benimports.com.br/IMG_2/ABC123.jpg
```

A mesma regra é aplicada às pastas `IMG_3` até `IMG_9`.

## Verificação das imagens

Antes de gerar cada URL, o sistema verifica se o arquivo correspondente existe na pasta esperada.

- Se o arquivo existir, o link será gerado.
- Se o arquivo não existir, a célula correspondente ficará vazia.

## Planilha de saída

A planilha gerada possui as seguintes colunas:

```text
SKU
IMAGEM_PRODUTO_1
IMAGEM_PRODUTO_2
IMAGEM_PRODUTO_3
IMAGEM_PRODUTO_4
IMAGEM_PRODUTO_5
IMAGEM_PRODUTO_6
IMAGEM_PRODUTO_7
IMAGEM_PRODUTO_8
IMAGEM_PRODUTO_9
STATUS
```

## Status do processamento

Quando todas as imagens do produto são encontradas, o status será:

```
OK
```

Quando alguma imagem não for encontrada, o status indicará as colunas correspondentes.

Exemplo:

```
Faltando links para as pastas: IMG_1, IMG_5, IMG_7
```

No resultado, `IMG_1` corresponde à coluna `IMAGEM_PRODUTO_1`.

## Estrutura do projeto

```text
Gerador-de-Link-ERP/
├── main.py
├── gui.py
├── Gerador de Links ERP.spec
├── installer/
│   └── gerador_links.iss
├── services/
│   ├── excel_service.py
│   ├── imagem_service.py
│   ├── link_service.py
│   ├── processamento_service.py
│   └── status_service.py
└── testes/
    └── testes_backend.py
```

- `main.py`: inicia a aplicação.
- `gui.py`: contém a interface gráfica e integra suas ações aos serviços.
- `excel_service.py`: realiza a leitura e a exportação das planilhas.
- `imagem_service.py`: monta nomes de arquivos e verifica a existência das imagens.
- `link_service.py`: gera as URLs das imagens encontradas.
- `processamento_service.py`: processa os SKUs e organiza o resultado final.
- `status_service.py`: informa quais imagens não foram encontradas.
- `Gerador de Links ERP.spec`: configura a criação do aplicativo com PyInstaller.
- `gerador_links.iss`: configura a criação do instalador com Inno Setup.

## Download e instalação

A versão pronta para uso é distribuída pela página de [Releases do projeto](https://github.com/cadu-cruz/Gerador-de-Link-ERP/releases).

Para instalar:

1. Acesse a página de Releases.
2. Abra a versão mais recente disponível.
3. Na seção **Assets**, baixe o arquivo `Gerador-de-Links-ERP-1.0.0.exe`.
4. Execute o arquivo baixado e siga as etapas do instalador.
5. Ao finalizar, abra o programa pelo menu Iniciar ou pelo atalho da área de trabalho, caso tenha escolhido criá-lo.

O instalador já inclui o Python e todas as bibliotecas necessárias. O usuário não precisa instalar Python, Pandas ou CustomTkinter separadamente.

> Esta versão foi desenvolvida para Windows. Como o instalador ainda não possui assinatura digital, o sistema operacional pode identificá-lo como sendo de um editor desconhecido. Confirme sempre que o arquivo foi obtido pela página oficial deste projeto antes de executá-lo.

## Executar a partir do código-fonte

Esta opção é destinada ao desenvolvimento do projeto.

Instale as dependências do projeto:

```bash
pip install customtkinter pandas openpyxl
```

Depois, na pasta principal do projeto, execute:

```bash
python main.py
```

> A funcionalidade **Abrir resultado** utiliza recursos do Windows. Esta versão do projeto foi desenvolvida para esse sistema operacional.
