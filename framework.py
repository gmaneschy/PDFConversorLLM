import os
from tkinter.filedialog import askopenfilenames

import requests
from tkinter import *


def selection():
    selecao = askopenfilenames(filetypes=[("Arquivos PDF", "*.pdf")])
    if selecao:
        # Atualiza o texto do label com os nomes dos arquivos selecionados
        nomes_arquivos = "\n".join([os.path.basename(arquivo) for arquivo in selecao])
        arquivos_selecionados.config(text=nomes_arquivos)


janela = Tk()
janela.title("Conversor de PDF")
janela.geometry("300x500")

# Configura colunas para centralização
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=2)
janela.grid_columnconfigure(2, weight=1)

# Texto superior
texto_orientacao = Label(janela, text="Selecione os PDFs para conversão")
texto_orientacao.grid(column=1, row=0, padx=10, pady=10)

# Botão
botao = Button(janela, text="SELECIONAR", command=selection)
botao.grid(column=1, row=1, padx=10, pady=10)


titulo = Label(janela, text="Arquivos selecionados:", font=("Arial", 10, "bold"))
titulo.grid(column=1, row=2, padx=25, pady=(10, 0))

arquivos_selecionados = Label(janela, text="", justify="left", anchor="w")
arquivos_selecionados.grid(column=1, row=3, padx=25, pady=5, sticky="w")

# Botão de conversão
botao_conversao = Button(janela, text="CONVERTER", command=lambda: os.system("main.py"))
botao_conversao.grid(column=1, row=4, padx=10, pady=10)


# mainloop() é sempre a última linha de código
janela.mainloop()