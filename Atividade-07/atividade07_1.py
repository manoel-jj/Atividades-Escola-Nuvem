import pandas as pd

arquivo = input("Digite o nome do arquivo CSV: ")

try:
    df = pd.read_csv(arquivo)

    media = df["tempo_execucao"].mean()
    desvio_padrao = df["tempo_execucao"].std()

    print("Média do tempo de execução:", round(media, 2))
    print("Desvio padrão:", round(desvio_padrao, 2))

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
except KeyError:
    print("Erro: coluna 'tempo_execucao' não existe no arquivo.")
except Exception:
    print("Erro ao ler o arquivo.")
