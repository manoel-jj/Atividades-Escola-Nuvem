num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("+ para soma")
print("- para subtração")
print("* para multiplicação")
print("/ para divisão")

operacao = input("Digite a operação: ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero!")
        resultado = None
else:
    print("Operação inválida!")
    resultado = None

if resultado is not None:
    print("Resultado:", resultado)