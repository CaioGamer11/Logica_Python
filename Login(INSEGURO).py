User= input("Digite seu usu�rio...")
Password= int(input("Digite sua senha(Somente n�meros)..."))
if User == 'Caio':
    if Password == 1234567890:
        print("Voc� est� logado com sucesso.")
    else:
        print("Senha incorreta.")
else:
    print("Usu�rio incorreto.")
#N�O USAR ESTE TIPO DE COMANDO, POR 2 MOTIVOS: 1- H� MUITO C�DIGO, 2- VOC� ENFRAQUECE A SENHA/LOGIN, FACILITANDO A INVAS�O.