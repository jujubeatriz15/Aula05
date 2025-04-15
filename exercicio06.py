pin = 1234
i= 1
senha = int(input("Digite a senha: "))
while senha != pin and i <= 2:
    senha = int(input("Digite a senha novamente: "))
    i += 1

if senha == pin:
    print("senha correta")
else:
    print("senha errada seu animal")
