import csv

arquivo = input("Digite o nome do arquivo CSV para salvar: ")

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 25, "São Paulo"],
    ["Carlos", 30, "Rio de Janeiro"],
    ["Mariana", 22, "Belo Horizonte"]
]

try:
    with open(arquivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerows(dados)

    print("Arquivo CSV criado com sucesso.")

except Exception:
    print("Erro ao salvar o arquivo CSV.")
