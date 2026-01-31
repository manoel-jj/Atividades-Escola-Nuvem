import json

arquivo = input("Digite o nome do arquivo JSON: ")

dados = {
    "nome": "João",
    "idade": 28,
    "cidade": "Curitiba"
}

try:
    # Escrita no arquivo JSON
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    # Leitura do arquivo JSON
    with open(arquivo, "r", encoding="utf-8") as f:
        dados_lidos = json.load(f)

    print("Dados lidos do arquivo JSON:")
    print(dados_lidos)

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception:
    print("Erro ao salvar ou ler o arquivo JSON.")
