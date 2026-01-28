import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url)
    resposta.raise_for_status()

    dados = resposta.json()
    usuario = dados["results"][0]

    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("Nome:", nome)
    print("Email:", email)
    print("País:", pais)

except requests.exceptions.RequestException:
    print("Falha ao conectar à API de usuários.")
