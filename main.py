import os

os.environ["LLAMA_CLOUD_API_KEY"] = ""
"""
import nest_asyncio
nest_asyncio.apply()
rodar antes do parse no jupyter
"""
from llama_parse import LlamaParse # Parse para traduzir informações de pdf para texto

# noinspection PyTypeChecker
documentos = LlamaParse(result_type="text", system_prompt="This file contains text. I'd like to get only the text from the file.", language="en").load_data("nome_do_arquivo.pdf")

print(len(documentos))

for i, pagina in enumerate(documentos):
    with open(f"meu_pdf/pagina{i+1}.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(pagina.text)