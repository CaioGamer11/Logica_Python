User= input("Digite seu usuário...")
Password= int(input("Digite sua senha(Somente números)..."))
if User == 'Caio':
    if Password == 1234567890:
        print("Você está logado com sucesso.")
    else:
        print("Senha incorreta.")
else:
    print("Usuário incorreto.")
#NÃO USAR ESTE TIPO DE COMANDO, POR 2 MOTIVOS: 1- HÁ MUITO CÓDIGO, 2- VOCÊ ENFRAQUECE A SENHA/LOGIN, FACILITANDO A INVASÃO.