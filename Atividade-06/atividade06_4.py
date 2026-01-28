import requests
from datetime import datetime

moeda = input("Digite o código da moeda (ex: USD, EUR): ").upper()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()
    chave = f"{moeda}BRL"

    if chave not in dados:
        print("Moeda não encontrada.")
    else:
        info = dados[chave]

        print("Moeda:", moeda)
        print("Valor atual:", info["bid"])
        print("Máxima:", info["high"])
        print("Mínima:", info["low"])

        data_hora = datetime.fromtimestamp(int(info["timestamp"]))
        print("Última atualização:", data_hora)

except requests.exceptions.RequestException:
    print("Erro ao consultar a moeda.")
