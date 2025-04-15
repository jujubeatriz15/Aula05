i = 0
n = 0
soma = 0
alunos = int(input("Digite a quantidade de alunos: "))
while i < alunos:
    v = float(input("digite os valores: "))
    soma = soma + v
    i = i + 1
    m = soma / alunos
print(m)