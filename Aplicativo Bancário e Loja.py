Aplicativo_Atual = "Nenhum" # Pode ser  Nenhum, Banco ,Loja ou Erro
Loop = False
UserCorreto = "Caio"
SenhaCorreta = "1234567890A"
saldo = 0
SairBanco = False
Carrinho_Compras = []
Total_Compra = 0
print('Seja bem-vindo(a) ao sistema Tem de Tudo!')
#Sistema de Login
print('')
UserDigitado = input('Digite seu nome de usu�rio: ')
SenhaDigitado = input('Digite sua senha: ')
if (UserDigitado == UserCorreto) and (SenhaCorreta == SenhaDigitado):
    Loop = True
    print('Voc� foi logado com sucesso.')
    saldo = 500
else:
    Loop = False
    print('Senha ou Usu�rio inv�lidos.')
while Loop == True:
    print(''' 
O que voc� deseja fazer?
    
1- Aplicativo Bancario
2- Loja Virtual
3- Sair do Sistema
    ''')
    resp = int( input('Digite o n�mero: ') )
    if resp == 1:
        Aplicativo_Atual = "Banco"
    elif resp == 2:    
        Aplicativo_Atual = "Loja"
    elif resp == 3:
        Aplicativo_Atual = "Nenhum"
        Loop = False
    else:
        Aplicativo_Atual = "Erro"
        Loop = False
    while Aplicativo_Atual == "Banco":
            opcao = int(input("""
Ol�! O que voc� deseja fazer?

1- Depositar
2- Sacar
3- Consultar
4- Sair

Escreva o n�mero da fun��o: """))
            if opcao == 1:
                valordepositado = int(input("Quantos reais voc� deseja depositar? R$"))
                saldo += valordepositado
                valordepositado = 0
            elif opcao == 2:
                valorsacado = int(input("Quantos reais deseja sacar? R$"))
                if saldo >= valorsacado:
                    saldo -= valorsacado
                else:
                    print("Saldo insuficiente.")
            elif opcao == 3:
                print("R$", saldo)
            elif opcao == 4:
                Aplicativo_Atual = "Nenhum"

    while Aplicativo_Atual == "Loja":
        opcao1 = int(input("""Ol�! O que voc� deseja fazer?
        
1- Comprar
2- Esvaziar Carrinho
3- Vizualizar Carrinho
4- Finalizar Compra
5- Sair

Digite o n�mero da fun��o: """))
        if opcao1 == 1:
            opcao2 = int(input("""Qual categoria de itens voc� deseja?
    
1- Comidas
2- Produtos de Beleza
3- Brinquedos
4- Roupas
5- Produtos de Limpeza

Escreva o n�mero da sua categoria: """))
            if opcao2 == 1:
                opcao3 = int(input("""Qual item voc� deseja comprar?

1- Arroz R$10,00
2- Feij�o R$7,00
3- Alface R$9,00
4- Tomate R$15,00
5- Cebola R$10,00

Escreva o n�mero do seu item: """))
                if opcao3 == 1:
                    Carrinho_Compras.append("Arroz")
                    Total_Compra += 10
                    print("Voc� adicionou arroz ao carrinho de compras.")
                elif opcao3 == 2:
                    Carrinho_Compras.append("Feij�o")
                    Total_Compra += 7
                    print("Voc� adicionou feij�o ao carrinho de compras.")
                elif opcao3 == 3:
                    Carrinho_Compras.append("Alface")
                    Total_Compra += 9
                    print("Voc� adicionou alface ao carrinho de compras.")
                elif opcao3 == 4:
                    Carrinho_Compras.append("Tomate")
                    Total_Compra += 15
                    print("Voc� adicionou tomate ao carrinho de compras.")
                elif opcao3 == 5:
                    Carrinho_Compras.append("Cebola")
                    Total_Compra += 10
                    print("Voc� adicionou cebola ao carrinho de compras.")
                else:
                    print("Este n�o � um item v�lido.")
            elif opcao2 == 2:
                opcao3 = int(input("""Qual item voc� deseja comprar?

1- Shampoo R$12,00
2- Condicionador R$13,00
3- Kit de Maquiagem R$20,00
4- Sabonete R$5,00
5- Barbeador R$5,00

Escreva o n�mero do seu item: """))
                if opcao3 == 1:
                    Carrinho_Compras.append("Shampoo")
                    Total_Compra += 12
                    print("Voc� adicionou shampoo ao carrinho de compras.")
                elif opcao3 == 2:
                    Carrinho_Compras.append("Condicionador")
                    Total_Compra += 13
                    print("Voc� adicionou condicionador ao carrinho de compras.")
                elif opcao3 == 3:
                    Carrinho_Compras.append("Kit de Maquiagem")
                    Total_Compra += 20
                    print("Voc� adicionou kit de maquiagem ao carrinho de compras.")
                elif opcao3 == 4:
                    Carrinho_Compras.append("Sabonete")
                    Total_Compra += 5
                    print("Voc� adicionou sabonete ao carrinho de compras.")
                elif opcao3 == 5:
                    Carrinho_Compras.append("Barbeador")
                    Total_Compra += 5
                    print("Voc� adicionou barbeador ao carrinho de compras.")
                else:
                    print("Este n�o � um item v�lido.")
            elif opcao2 == 3:
                opcao3 = int(input("""Qual item voc� deseja comprar?

1- Trenzinho de Brinquedo R$10,00
2- Boneca R$15,00
3- Carrinho R$7,00
4- Kit de Brinquedos de Areia R$17,00
5- Cozinha de Brinquedo R$20,00

Escreva o n�mero do seu item: """))
                if opcao3 == 1:
                    Carrinho_Compras.append("Trenzinho de Brinquedo")
                    Total_Compra += 10
                    print("Voc� adicionou trenzinho de brinquedo ao carrinho de compras.")
                elif opcao3 == 2:
                    Carrinho_Compras.append("Boneca")
                    Total_Compra += 15
                    print("Voc� adicionou boneca ao carrinho de compras.")
                elif opcao3 == 3:
                    Carrinho_Compras.append("Carrinho")
                    Total_Compra += 7
                    print("Voc� adicionou carrinho ao carrinho de compras.")
                elif opcao3 == 4:
                    Carrinho_Compras.append("Kit de Brinquedos de Areia")
                    Total_Compra += 17
                    print("Voc� adicionou kit de brinquedos de areia ao carrinho de compras.")
                elif opcao3 == 5:
                    Carrinho_Compras.append("Cozinha de Brinquedo")
                    Total_Compra += 20
                    print("Voc� adicionou cozinha de brinquedo ao carrinho de compras.")
                else:
                    print("Este n�o � um item v�lido.")
            elif opcao2 == 4:
                opcao3 = int(input("""Qual item voc� deseja comprar?

1- Camiseta R$10,00
2- Cal�a R$7,00
3- T�nis R$8,00
4- Sapato R$8,00
5- Shorts R$5,00
6- Blusa R$15,00
7- Camiseta Manga Comprida  R$12,00
8- Regata R$7,00

Escreva o n�mero do seu item: """))
                if opcao3 == 1:
                    Carrinho_Compras.append("Camiseta")
                    Total_Compra += 10
                    print("Voc� adicionou camiseta ao carrinho de compras.")
                elif opcao3 == 2:
                    Carrinho_Compras.append("Cal�a")
                    Total_Compra += 7
                    print("Voc� adicionou cal�a ao carrinho de compras.")
                elif opcao3 == 3:
                    Carrinho_Compras.append("T�nis")
                    Total_Compra += 8
                    print("Voc� adicionou t�nis ao carrinho de compras.")
                elif opcao3 == 4:
                    Carrinho_Compras.append("Sapato")
                    Total_Compra += 8
                    print("Voc� adicionou sapato ao carrinho de compras.")
                elif opcao3 == 5:
                    Carrinho_Compras.append("Shorts")
                    Total_Compra += 5
                    print("Voc� adicionou shorts ao carrinho de compras.")
                elif opcao3 == 6:
                    Carrinho_Compras.append("Blusa")
                    Total_Compra += 15
                    print("Voc� adicionou blusa ao carrinho de compras.")
                elif opcao3 == 7:
                    Carrinho_Compras.append("Camiseta Manga Comprida")
                    Total_Compra += 12
                    print("Voc� adicionou camiseta manga comprida ao carrinho de compras.")
                elif opcao3 == 8:
                    Carrinho_Compras.append("Regata")
                    Total_Compra += 7
                    print("Voc� adicionou regata ao carrinho de compras.")
                else:
                    print("Este n�o � um item v�lido.")
            elif opcao2 == 5:
                opcao3 = int(input("""Qual item voc� deseja comprar?

1- Vassoura R$5,00
2- Esfreg�o  R$5,00
3- Alvejante R$10,00
4- Balde R$7,00
5- Detergente R$2,00

Escreva o n�mero do seu item: """))
                if opcao3 == 1:
                    Carrinho_Compras.append("Vassoura")
                    Total_Compra += 5
                    print("Voc� adicionou vassoura ao carrinho de compras.")
                elif opcao3 == 2:
                    Carrinho_Compras.append("Esfreg�o")
                    Total_Compra += 5
                    print("Voc� adicionou esfreg�o ao carrinho de compras.")
                elif opcao3 == 3:
                    Carrinho_Compras.append("Alvejante")
                    Total_Compra += 10
                    print("Voc� adicionou alvejante de compras.")
                elif opcao3 == 4:
                    Carrinho_Compras.append("Balde")
                    Total_Compra += 7
                    print("Voc� adicionou balde ao carrinho de compras.")
                elif opcao3 == 5:
                    Carrinho_Compras.append("Detergente")
                    Total_Compra += 2
                    print("Voc� adicionou detergente ao carrinho de compras.")
                else:
                    print("Este n�o � um item v�lido.")
            else:
                print("Esta n�o � uma categoria v�lida.")
        elif opcao1 == 2:
            opcao4 = int(input("""Voc� deseja:
                
1- Esvaziar totalmente o carrinho
2- Retirar um item do carrinho

Digite o n�mero da fun��o: """))
            if opcao4 == 1:
                Carrinho_Compras.clear()
                print("Carrinho esvaziado com sucesso.")
            elif (opcao4 == 2):
                Remover = input("Digite o nome do item a ser removido: ")
                if Remover in Carrinho_Compras:
                    Carrinho_Compras.remove(Remover)
                    print("Item removido com sucesso")
                else:
                    print("Este item n�o est� dentro de seu carrinho de compras.")
            else:
                print("Esta op��o n�o � v�lida.")
        elif opcao1 == 3:
            print(Carrinho_Compras)
        elif opcao1 == 4:
            if (saldo >= Total_Compra):
                print("Compra finalizada com sucesso!")
                Carrinho_Compras.clear()
                saldo -= Total_Compra
                Total_Compra = 0
            else:
                print("Saldo insuficiente.")
        elif opcao1 == 5:
            Aplicativo_Atual = "Nenhum"
        else:
            print("Fun��o inv�lida.")
if Aplicativo_Atual == "Erro":
    print('Voc� escolheu uma op��o inv�lida!')
else:
    print('')