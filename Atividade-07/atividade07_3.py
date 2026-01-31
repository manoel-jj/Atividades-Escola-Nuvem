import csv

arquivo = input("Digite o nome do arquivo CSV: ")

try:
    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.reader(f)

        for linha in leitor:
            print(linha)

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except Exception:
    print("Erro ao ler o arquivo.")
