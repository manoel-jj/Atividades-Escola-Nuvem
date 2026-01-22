
def calcular_preco_desconto(preco_original, percentual_desconto):
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return round(preco_final, 2)


preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite a porcentagem de desconto: "))

preco_final = calcular_preco_desconto(preco, desconto)
print("Preço final com desconto: R$", preco_final)
