quantidade = int(input("Quantos alunos existem na turma? "))

soma_notas = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma_notas += nota

media = soma_notas / quantidade

print("Média da turma:", round(media, 2))