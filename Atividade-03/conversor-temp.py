temperatura = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Unidade de destino (C, F, K): ").upper()

if origem == "C" and destino == "F":
    resultado = (temperatura * 9/5) + 32
elif origem == "C" and destino == "K":
    resultado = temperatura + 273.15
elif origem == "F" and destino == "C":
    resultado = (temperatura - 32) * 5/9
elif origem == "F" and destino == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15
elif origem == "K" and destino == "C":
    resultado = temperatura - 273.15
elif origem == "K" and destino == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32
else:
    resultado = temperatura  # mesma unidade

print("Temperatura convertida:", round(resultado, 2))