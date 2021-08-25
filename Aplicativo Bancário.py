sair = False
saldo = 500
user= input("Digite seu usuário...")
Password= int(input("Digite sua senha...(Somente números!)"))
logado = False
if (user == "Caio" ) and (Password==1234567890):
    print("Você está logado com sucesso.")
    logado = True
else:
    print("Login ou senha incorretos.")

while not(sair) and (logado == True):
    opcao = int(input("Olá, o que deseja fazer? 1 - Depositar, 2 - Sacar, 3 - Consultar, 4 - Sair "))
    if opcao == 1:
        valor_depositado = int(input("Quantos reais deseja depositar? R$"))
        saldo += valor_depositado
    elif opcao == 2:
        valor_sacado = int(input("Quantos reais deseja sacar? R$"))
        if (saldo >= valor_sacado):
            saldo -= valor_sacado
        else:
            print("Saldo insuficiente.")
    elif opcao == 3:
        print("Seu saldo é de R$", saldo)
    elif opcao == 4:
        sair = True
        print("Tchau tchau!")
    else:
        print("Esta não é uma opção válida.")