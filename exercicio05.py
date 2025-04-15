valor1 = int(input("digite o primeiro valor: "))
valor2 = int(input("digite o segundo valor: "))

while valor2 == 0:
    valor2 = int(input("digite o segundo valor novamente: "))
divisao = valor1 / valor2
print(divisao)