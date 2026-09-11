import customtkinter as ctk
from tkinter import filedialog
from pathlib import Path


class GeradorLinksApp(ctk.CTk):
    COR_LARANJA = "#F28C28"
    COR_LARANJA_HOVER = "#D97706"

    def __init__(self):
        super().__init__()

        self.title("Gerador de Links ERP")
        self.geometry("700x700")

        self.caminho_planilha = None
        self.pasta_fotos = None

        self.criar_widgets()

    def criar_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        painel = ctk.CTkFrame(self, corner_radius=14)
        painel.grid(row=0, column=0, padx=20, pady=18, sticky="nsew")
        painel.grid_columnconfigure(1, weight=1)
        painel.grid_rowconfigure(8, weight=1)

        titulo = ctk.CTkLabel(
            painel,
            text="Ben Imports",
            font=ctk.CTkFont(size=25, weight="bold"),
            text_color=self.COR_LARANJA,
        )
        titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(14, 0))

        subtitulo = ctk.CTkLabel(
            painel,
            text="Geração de URLs de imagens para importação no ERP",
            font=ctk.CTkFont(size=13),
            text_color=("gray35", "gray70"),
        )
        subtitulo.grid(row=1, column=0, columnspan=2, padx=20, pady=(2, 12))

        self.botao_planilha = self.criar_botao(
            painel,
            texto="SELECIONAR PLANILHA",
            comando=self.selecionar_planilha,
        )
        self.botao_planilha.grid(row=2, column=0, padx=(20, 12), pady=5, sticky="w")

        self.label_planilha = ctk.CTkLabel(
            painel,
            text="Nenhuma planilha selecionada",
            anchor="w",
            text_color=("gray40", "gray70"),
        )
        self.label_planilha.grid(row=2, column=1, padx=(0, 20), pady=5, sticky="ew")

        self.botao_pasta = self.criar_botao(
            painel,
            texto="SELECIONAR PASTA",
            comando=self.selecionar_pasta_fotos,
        )
        self.botao_pasta.grid(row=3, column=0, padx=(20, 12), pady=5, sticky="w")

        self.label_pasta = ctk.CTkLabel(
            painel,
            text="Nenhuma pasta selecionada",
            anchor="w",
            text_color=("gray40", "gray70"),
        )
        self.label_pasta.grid(row=3, column=1, padx=(0, 20), pady=5, sticky="ew")

        area_acoes = ctk.CTkFrame(painel, fg_color="transparent")
        area_acoes.grid(
            row=4,
            column=0,
            columnspan=2,
            padx=20,
            pady=(12, 6),
            sticky="w",
        )

        self.botao_gerar = self.criar_botao(
            area_acoes,
            texto="GERAR LINKS",
            comando=self.iniciar_carregamento_visual,
            state="disabled",
        )
        self.botao_gerar.grid(row=0, column=0, padx=(0, 6))

        self.botao_cancelar = self.criar_botao(
            area_acoes,
            texto="CANCELAR",
            comando=self.destroy,
        )
        self.botao_cancelar.grid(row=0, column=1, padx=(6, 0))

        self.barra_progresso = ctk.CTkProgressBar(
            painel,
            mode="determinate",
            progress_color=self.COR_LARANJA,
        )
        self.barra_progresso.grid(
            row=5,
            column=0,
            columnspan=2,
            padx=20,
            pady=(2, 6),
            sticky="ew",
        )
        self.barra_progresso.set(0)

        self.botao_abrir_resultado = self.criar_botao(
            painel,
            texto="Abrir resultado",
            largura=130,
            altura=26,
            state="disabled",
        )
        self.botao_abrir_resultado.grid(
            row=6,
            column=0,
            padx=20,
            pady=(0, 7),
            sticky="w",
        )

        label_log = ctk.CTkLabel(
            painel,
            text="Log de processamento",
            font=ctk.CTkFont(size=13, weight="bold"),
            anchor="w",
        )
        label_log.grid(row=7, column=0, columnspan=2, padx=20, sticky="ew")

        self.campo_log = ctk.CTkTextbox(
            painel,
            corner_radius=8,
            height=65,
            state="disabled",
        )
        self.campo_log.grid(
            row=8,
            column=0,
            columnspan=2,
            padx=20,
            pady=(4, 14),
            sticky="nsew",
        )

    def criar_botao(
        self,
        master,
        texto,
        comando=None,
        largura=175,
        altura=32,
        state="normal",
    ):
        return ctk.CTkButton(
            master,
            text=texto,
            command=comando,
            width=largura,
            height=altura,
            state=state,
            fg_color=self.COR_LARANJA,
            hover_color=self.COR_LARANJA_HOVER,
            text_color="white",
        )

    def selecionar_planilha(self):
        caminho = filedialog.askopenfilename(
            title="Selecione a planilha",
            filetypes=[("Arquivos Excel", "*.xlsx")],
        )
        if not caminho:
            return

        self.caminho_planilha = caminho
        self.label_planilha.configure(text=Path(caminho).name)
        self.atualizar_status_botao()

    def selecionar_pasta_fotos(self):
        pasta = filedialog.askdirectory(
            title="Selecione a pasta de fotos",
            mustexist=True,
        )
        if not pasta:
            return

        self.pasta_fotos = pasta
        self.label_pasta.configure(text=Path(pasta).name)
        self.atualizar_status_botao()

    def atualizar_status_botao(self):
        estado = (
            "normal"
            if self.caminho_planilha and self.pasta_fotos
            else "disabled"
        )
        self.botao_gerar.configure(state=estado)

    def iniciar_carregamento_visual(self):
        self.barra_progresso.stop()
        self.barra_progresso.configure(mode="indeterminate")
        self.barra_progresso.start()
