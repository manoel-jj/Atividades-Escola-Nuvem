def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    """
    Calcula o valor da gorjeta baseado na conta e na porcentagem desejada.
    :param valor_conta: float - valor total da conta
    :param porcentagem_gorjeta: float - porcentagem da gorjeta (ex: 10)
    :return: float - valor da gorjeta
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

valor_gorjeta = calcular_gorjeta(valor, porcentagem)
print("Valor da gorjeta: R$", round(valor_gorjeta, 2))
