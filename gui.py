import customtkinter as ctk
from tkinter import filedialog, messagebox
from services.excel_service import ler_planilha, salvar_planilha
from services.processamento_service import processar_dados
from pathlib import Path
from threading import Thread
import os

ctk.set_appearance_mode("light")


class GeradorLinksApp(ctk.CTk):
    COR_LARANJA = "#F97316"
    COR_LARANJA_HOVER = "#EA580C"

    def __init__(self):
        super().__init__()

        self.title("Gerador de Links ERP")
        self.geometry("700x700")
        self.configure(fg_color="#FFFFFF")

        self.caminho_planilha = None
        self.pasta_fotos = None
        self.caminho_resultado = None

        self.criar_widgets()

    def criar_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        painel = ctk.CTkFrame(
            self,
            corner_radius=14,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#E5E7EB",
        )
        painel.grid(row=0, column=0, padx=20, pady=18, sticky="nsew")
        painel.grid_columnconfigure(1, weight=1)
        painel.grid_rowconfigure(9, weight=1)

        titulo = ctk.CTkLabel(
            painel,
            text="Gerador de Links ERP",
            font=ctk.CTkFont(size=25, weight="bold"),
            text_color=self.COR_LARANJA,
        )
        titulo.grid(row=0, column=0, columnspan=2, padx=20, pady=(14, 0))

        subtitulo = ctk.CTkLabel(
            painel,
            text="Geração de URLs de imagens para importação no ERP",
            font=ctk.CTkFont(size=13),
            text_color="#64748B",
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
            text_color="#475569",
        )
        self.label_planilha.grid(row=2, column=1, padx=(0, 20), pady=5, sticky="ew")

        aviso_planilha = ctk.CTkLabel(
            painel,
            text="Importante: a planilha deve conter uma coluna chamada SKU.",
            font=ctk.CTkFont(size=11),
            anchor="w",
            text_color="#C2410C",
        )
        aviso_planilha.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=20,
            pady=(0, 6),
            sticky="ew",
        )

        self.botao_pasta = self.criar_botao(
            painel,
            texto="SELECIONAR PASTA",
            comando=self.selecionar_pasta_fotos,
        )
        self.botao_pasta.grid(row=4, column=0, padx=(20, 12), pady=5, sticky="w")

        self.label_pasta = ctk.CTkLabel(
            painel,
            text="Nenhuma pasta selecionada",
            anchor="w",
            text_color="#475569",
        )
        self.label_pasta.grid(row=4, column=1, padx=(0, 20), pady=5, sticky="ew")

        area_acoes = ctk.CTkFrame(painel, fg_color="transparent")
        area_acoes.grid(
            row=5,
            column=0,
            columnspan=2,
            padx=20,
            pady=(12, 6),
            sticky="w",
        )

        self.botao_gerar = self.criar_botao(
            area_acoes,
            texto="GERAR LINKS",
            comando=self.iniciar_processamento,
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
            fg_color="#E5E7EB",
        )
        self.barra_progresso.grid(
            row=6,
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
            comando=self.abrir_resultado,
            largura=130,
            altura=26,
            state="disabled",
        )
        self.botao_abrir_resultado.grid(
            row=7,
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
            text_color="#334155",
        )
        label_log.grid(row=8, column=0, columnspan=2, padx=20, sticky="ew")

        self.campo_log = ctk.CTkTextbox(
            painel,
            corner_radius=8,
            height=65,
            state="disabled",
            fg_color="#F8FAFC",
            text_color="#1F2937",
            border_width=1,
            border_color="#E5E7EB",
        )
        self.campo_log.grid(
            row=9,
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
            corner_radius=8,
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

    # Libera o campo, adiciona a mensagem no final e o bloqueia novamente
    def adicionar_log(self, mensagem):
        self.campo_log.configure(state="normal")
        self.campo_log.insert("end", mensagem + "\n")
        self.campo_log.see("end")
        self.campo_log.configure(state="disabled")

    # Solicita o local de saída, prepara a interface e inicia
    # o processamento em uma thread separada para não travar a janela
    def iniciar_processamento(self):
        caminho_planilha = self.caminho_planilha
        pasta_fotos = self.pasta_fotos

        self.botao_gerar.configure(state="disabled")
        self.botao_abrir_resultado.configure(state="disabled")
        self.caminho_resultado = None

        self.iniciar_carregamento_visual()
        self.adicionar_log("Iniciando processamento...")

        self.thread_processamento = Thread(
            target=self.executar_processamento,
            args=(caminho_planilha, pasta_fotos),
            daemon=True,
        )
        self.thread_processamento.start()

    # Executa os serviços de leitura, processamento e salvamento em segundo plano,
    # solicitando que a interface mostre o resultado ou o erro na thread principal.
    def executar_processamento(
    self,
    caminho_planilha,
    pasta_fotos,
    ):
        try:
            # Lê a planilha e devolve seus dados em um DataFrame
            dados = ler_planilha(caminho_planilha)

            self.after(
                0,
                self.adicionar_log,
                f"{len(dados)} linhas encontradas"
            )

            # Processa os SKUs e cria o DataFrame de resultado
            resultado = processar_dados(dados, pasta_fotos)
        except Exception as erro:
            self.after(0, self.finalizar_com_erro, str(erro))

        else:
            self.after(
                0,
                self.solicitar_salvamento,
                resultado,
                caminho_planilha,
            )

    def solicitar_salvamento(self, resultado, caminho_planilha):
        self.barra_progresso.stop()
        self.barra_progresso.configure(mode="determinate")
        self.barra_progresso.set(0.8)

        arquivo_entrada = Path(caminho_planilha)

        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar planilha de resultado",
            initialdir=str(arquivo_entrada.parent),
            initialfile=f"{arquivo_entrada.stem}_resultado.xlsx",
            defaultextension=".xlsx",
            filetypes=[("Arquivos Excel", "*.xlsx")],
        )

        if not caminho_saida:
            self.barra_progresso.set(0)
            self.atualizar_status_botao()
            self.adicionar_log(
                "Links gerados, mas o salvamento foi cancelado."
            )
            return

        self.adicionar_log("Salvando planilha de resultado...")

        self.thread_salvamento = Thread(
            target=self.executar_salvamento,
            args=(resultado, caminho_saida),
            daemon=True,
        )
        self.thread_salvamento.start()

    def executar_salvamento(self, resultado, caminho_saida):
        try:
            caminho_resultado = salvar_planilha(
                resultado,
                caminho_saida,
            )

        except Exception as erro:
            self.after(0, self.finalizar_com_erro, str(erro))

        else:
            self.after(
                0,
                self.finalizar_com_sucesso,
                caminho_resultado,
                len(resultado),
            )

    # Atualiza a interface após o processamento terminar com sucesso,
    # guardando o resultado e reabilitando as ações disponíveis.
    def finalizar_com_sucesso(self, caminho_resultado, quantidade):
        # Guarda o caminho para permitir que o resultado seja aberto depois
        self.caminho_resultado = caminho_resultado

        # Finaliza a animação e mostra a barra como concluída
        self.barra_progresso.stop()
        self.barra_progresso.configure(mode="determinate")
        self.barra_progresso.set(1)

        # Libera as ações da interface após o processamento
        self.botao_abrir_resultado.configure(state="normal")
        self.atualizar_status_botao()

        self.adicionar_log(
            f"Processamento concluído: {quantidade} produtos."
        )
        self.adicionar_log(
            f"Planilha salva em: {caminho_resultado}"
        )

        messagebox.showinfo(
            "Processamento concluído",
            f"{quantidade} produtos processados.",
        )

    # Restaura a interface e informa o usuário quando o processamento falha
    def finalizar_com_erro(self, mensagem):

        # Interrompe o carregamento e volta a barra ao estado inicial
        self.barra_progresso.stop()
        self.barra_progresso.configure(mode="determinate")
        self.barra_progresso.set(0)
        
        # Libera uma nova tentativa e registra o motivo da falha
        self.atualizar_status_botao()
        self.adicionar_log(f"Erro: {mensagem}")

        messagebox.showerror(
            "Erro no processamento",
            mensagem,
        )
    def abrir_resultado(self):
        if not self.caminho_resultado:
            messagebox.showwarning(
                "Resultado indisponível",
                "Nenhuma planilha de resultado foi gerada.",
            )
            return

        arquivo_resultado = Path(self.caminho_resultado)

        if not arquivo_resultado.is_file():
            messagebox.showerror(
                "Arquivo não encontrado",
                "A planilha de resultado não foi encontrada.",
            )
            return

        try:
            os.startfile(str(arquivo_resultado))
        except OSError as erro:
            messagebox.showerror(
                "Erro ao abrir resultado",
                str(erro),
            )
