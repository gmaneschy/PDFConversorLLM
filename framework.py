import os
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
from main import processar_pdfs

# Variável para guardar os arquivos selecionados
selected_files = []

def selection():
    global selected_files
    selected_files = askopenfilenames(filetypes=[("Arquivos PDF", "*.pdf")])
    if selected_files:
        nomes_arquivos = "\n".join([os.path.basename(arquivo) for arquivo in selected_files])
        arquivos_selecionados.config(text=nomes_arquivos)


def convert():
    try:
        if selected_files:
            total = len(selected_files)
            progress["maximum"] = total
            progress["value"] = 0
            janela.update()

            for i, arquivo in enumerate(selected_files):
                arquivos_selecionados.config(text=f"Convertendo: {os.path.basename(arquivo)} ({i+1}/{total})")
                janela.update()

                # Processa um arquivo por vez
                processar_pdfs([arquivo])

                progress["value"] += 1
                janela.update()

            arquivos_selecionados.config(text="Conversão concluída!")
        else:
            arquivos_selecionados.config(text="Nenhum arquivo selecionado.")
    except Exception as e:
        arquivos_selecionados.config(text=f"Erro: {e}")


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
botao_conversao = Button(janela, text="CONVERTER", command=convert)
botao_conversao.grid(column=1, row=4, padx=10, pady=10)
progress = ttk.Progressbar(janela, orient="horizontal", mode="determinate", length=200)
progress.grid(column=1, row=5, pady=20)
progress["value"] = 0

# mainloop() é sempre a última linha de código
janela.mainloop()