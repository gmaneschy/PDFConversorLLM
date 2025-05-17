import os

os.environ["LLAMA_CLOUD_API_KEY"] = "SUA CHAVE API"
"""
import nest_asyncio
nest_asyncio.apply()
rodar antes do parse no jupyter
"""
from llama_parse import LlamaParse # Parse para traduzir informações de pdf para texto

# noinspection PyTypeChecker
def processar_pdfs(lista_de_arquivos):
    os.makedirs("meu_pdf", exist_ok=True)
    documentos_por_arquivo = {}

    for arquivo in lista_de_arquivos:
        print(f"Processando: {arquivo}")
        documentos = LlamaParse(
            result_type="text",
            system_prompt=
                "This document may contain both embedded text and scanned images with overlapping content. "
                "Extract all the readable text using OCR if needed, but ensure that duplicate or repeated sentences are removed. "
                "Keep the natural reading order, correct OCR artifacts (e.g. wrong characters or line breaks), "
                "and output only a clean, unified version of the text, as if it were typed manually."
        ).load_data(arquivo)

        documentos_por_arquivo[arquivo] = documentos

        nome_base = os.path.splitext(os.path.basename(arquivo))[0]
        caminho_saida = f"meu_pdf/{nome_base}.txt"  # ou .md se quiser manter o formato

        with open(caminho_saida, "w", encoding="utf-8") as f:
            for pagina in documentos:
                f.write(pagina.text.strip())
                f.write("\n\n")  # separador entre páginas

    return documentos_por_arquivo