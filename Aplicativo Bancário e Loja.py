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
UserDigitado = input('Digite seu nome de usuário: ')
SenhaDigitado = input('Digite sua senha: ')
if (UserDigitado == UserCorreto) and (SenhaCorreta == SenhaDigitado):
    Loop = True
    print('Você foi logado com sucesso.')
    saldo = 500
else:
    Loop = False
    print('Senha ou Usuário inválidos.')
while Loop == True:
    print(''' 
O que você deseja fazer?
    
1- Aplicativo Bancario
2- Loja Virtual
3- Sair do Sistema
    ''')
    resp = int( input('Digite o número: ') )
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
Olá! O que você deseja fazer?

1- Depositar
2- Sacar
3- Consultar
4- Sair

Escreva o número da função: """))
            if opcao == 1:
                valordepositado = int(input("Quantos reais você deseja depositar? R$"))
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
        opcao1 = int(input("""Olá! O que você deseja fazer?
        
1- Comprar
2- Esvaziar Carrinho
3- Vizualizar Carrinho
4- Finalizar Compra
5- Sair

Digite o número da função: """))
        if opcao1 == 1:
            opcao2 = int(input("""Qual categoria de itens você deseja?
    
1- Comidas
2- Produtos de Beleza
3- Brinquedos
4- Roupas
5- Produtos de Limpeza

Escreva o número da sua categoria: """))
            if opcao2 == 1:
                opcao3 = int(input("""Qual item você deseja comprar?

1- Arroz R$10,00
2- Feijão R$7,00
3- Alface R$9,00
4- Tomate R$15,00
5- Cebola R$10,00

Escreva o número do seu item: """))
                if opcao3 == 1:
                    Carrinho_Compras.append("Arroz")
                    Total_Compra += 10
                    print("Você adicionou arroz ao carrinho de compras.")
                elif opcao3 == 2:
                    Carrinho_Compras.append("Feijão")
                    Total_Compra += 7
                    print("Você adicionou feijão ao carrinho de compras.")
                elif opcao3 == 3:
                    Carrinho_Compras.append("Alface")
                    Total_Compra += 9
                    print("Você adicionou alface ao carrinho de compras.")
                elif opcao3 == 4:
                    Carrinho_Compras.append("Tomate")
                    Total_Compra += 15
                    print("Você adicionou tomate ao carrinho de compras.")
                elif opcao3 == 5:
                    Carrinho_Compras.append("Cebola")
                    Total_Compra += 10
                    print("Você adicionou cebola ao carrinho de compras.")
                else:
                    print("Este não é um item válido.")
            elif opcao2 == 2:
                opcao3 = int(input("""Qual item você deseja comprar?

1- Shampoo R$12,00
2- Condicionador R$13,00
3- Kit de Maquiagem R$20,00
4- Sabonete R$5,00
5- Barbeador R$5,00

Escreva o número do seu item: """))
                if opcao3 == 1:
                    Carrinho_Compras.append("Shampoo")
                    Total_Compra += 12
                    print("Você adicionou shampoo ao carrinho de compras.")
                elif opcao3 == 2:
                    Carrinho_Compras.append("Condicionador")
                    Total_Compra += 13
                    print("Você adicionou condicionador ao carrinho de compras.")
                elif opcao3 == 3:
                    Carrinho_Compras.append("Kit de Maquiagem")
                    Total_Compra += 20
                    print("Você adicionou kit de maquiagem ao carrinho de compras.")
                elif opcao3 == 4:
                    Carrinho_Compras.append("Sabonete")
                    Total_Compra += 5
                    print("Você adicionou sabonete ao carrinho de compras.")
                elif opcao3 == 5:
                    Carrinho_Compras.append("Barbeador")
                    Total_Compra += 5
                    print("Você adicionou barbeador ao carrinho de compras.")
                else:
                    print("Este não é um item válido.")
            elif opcao2 == 3:
                opcao3 = int(input("""Qual item você deseja comprar?

1- Trenzinho de Brinquedo R$10,00
2- Boneca R$15,00
3- Carrinho R$7,00
4- Kit de Brinquedos de Areia R$17,00
5- Cozinha de Brinquedo R$20,00

Escreva o número do seu item: """))
                if opcao3 == 1:
                    Carrinho_Compras.append("Trenzinho de Brinquedo")
                    Total_Compra += 10
                    print("Você adicionou trenzinho de brinquedo ao carrinho de compras.")
                elif opcao3 == 2:
                    Carrinho_Compras.append("Boneca")
                    Total_Compra += 15
                    print("Você adicionou boneca ao carrinho de compras.")
                elif opcao3 == 3:
                    Carrinho_Compras.append("Carrinho")
                    Total_Compra += 7
                    print("Você adicionou carrinho ao carrinho de compras.")
                elif opcao3 == 4:
                    Carrinho_Compras.append("Kit de Brinquedos de Areia")
                    Total_Compra += 17
                    print("Você adicionou kit de brinquedos de areia ao carrinho de compras.")
                elif opcao3 == 5:
                    Carrinho_Compras.append("Cozinha de Brinquedo")
                    Total_Compra += 20
                    print("Você adicionou cozinha de brinquedo ao carrinho de compras.")
                else:
                    print("Este não é um item válido.")
            elif opcao2 == 4:
                opcao3 = int(input("""Qual item você deseja comprar?

1- Camiseta R$10,00
2- Calça R$7,00
3- Tênis R$8,00
4- Sapato R$8,00
5- Shorts R$5,00
6- Blusa R$15,00
7- Camiseta Manga Comprida  R$12,00
8- Regata R$7,00

Escreva o número do seu item: """))
                if opcao3 == 1:
                    Carrinho_Compras.append("Camiseta")
                    Total_Compra += 10
                    print("Você adicionou camiseta ao carrinho de compras.")
                elif opcao3 == 2:
                    Carrinho_Compras.append("Calça")
                    Total_Compra += 7
                    print("Você adicionou calça ao carrinho de compras.")
                elif opcao3 == 3:
                    Carrinho_Compras.append("Tênis")
                    Total_Compra += 8
                    print("Você adicionou tênis ao carrinho de compras.")
                elif opcao3 == 4:
                    Carrinho_Compras.append("Sapato")
                    Total_Compra += 8
                    print("Você adicionou sapato ao carrinho de compras.")
                elif opcao3 == 5:
                    Carrinho_Compras.append("Shorts")
                    Total_Compra += 5
                    print("Você adicionou shorts ao carrinho de compras.")
                elif opcao3 == 6:
                    Carrinho_Compras.append("Blusa")
                    Total_Compra += 15
                    print("Você adicionou blusa ao carrinho de compras.")
                elif opcao3 == 7:
                    Carrinho_Compras.append("Camiseta Manga Comprida")
                    Total_Compra += 12
                    print("Você adicionou camiseta manga comprida ao carrinho de compras.")
                elif opcao3 == 8:
                    Carrinho_Compras.append("Regata")
                    Total_Compra += 7
                    print("Você adicionou regata ao carrinho de compras.")
                else:
                    print("Este não é um item válido.")
            elif opcao2 == 5:
                opcao3 = int(input("""Qual item você deseja comprar?

1- Vassoura R$5,00
2- Esfregão  R$5,00
3- Alvejante R$10,00
4- Balde R$7,00
5- Detergente R$2,00

Escreva o número do seu item: """))
                if opcao3 == 1:
                    Carrinho_Compras.append("Vassoura")
                    Total_Compra += 5
                    print("Você adicionou vassoura ao carrinho de compras.")
                elif opcao3 == 2:
                    Carrinho_Compras.append("Esfregão")
                    Total_Compra += 5
                    print("Você adicionou esfregão ao carrinho de compras.")
                elif opcao3 == 3:
                    Carrinho_Compras.append("Alvejante")
                    Total_Compra += 10
                    print("Você adicionou alvejante de compras.")
                elif opcao3 == 4:
                    Carrinho_Compras.append("Balde")
                    Total_Compra += 7
                    print("Você adicionou balde ao carrinho de compras.")
                elif opcao3 == 5:
                    Carrinho_Compras.append("Detergente")
                    Total_Compra += 2
                    print("Você adicionou detergente ao carrinho de compras.")
                else:
                    print("Este não é um item válido.")
            else:
                print("Esta não é uma categoria válida.")
        elif opcao1 == 2:
            opcao4 = int(input("""Você deseja:
                
1- Esvaziar totalmente o carrinho
2- Retirar um item do carrinho

Digite o número da função: """))
            if opcao4 == 1:
                Carrinho_Compras.clear()
                print("Carrinho esvaziado com sucesso.")
            elif (opcao4 == 2):
                Remover = input("Digite o nome do item a ser removido: ")
                if Remover in Carrinho_Compras:
                    Carrinho_Compras.remove(Remover)
                    print("Item removido com sucesso")
                else:
                    print("Este item não está dentro de seu carrinho de compras.")
            else:
                print("Esta opção não é válida.")
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
            print("Função inválida.")
if Aplicativo_Atual == "Erro":
    print('Você escolheu uma opção inválida!')
else:
    print('')