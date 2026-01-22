
from datetime import date


ano = int(input("Ano de nascimento: "))
mes = int(input("Mês de nascimento: "))
dia = int(input("Dia de nascimento: "))

data_nascimento = date(ano, mes, dia)
hoje = date.today()

dias_vividos = (hoje - data_nascimento).days

print(f"Você está vivo(a) há {dias_vividos} dias.")
