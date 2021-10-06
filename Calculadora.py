def Soma(valor1, valor2):
    print("O total da conta desejada é:", valor1 + valor2)
def Subtracao(valor3, valor4):
    print("O total da conta desejada é:", valor3 - valor4)
def Multiplicacao(valor6, valor7):
    print("O total da conta desejada é:", valor6 * valor7)
def Divisao(valor8, valor9):
    print("O total da conta desejada é:", valor8 / valor9)
def Resto(valor10, valor11):
    print("O total da conta desejada é:", valor10 % valor11)
def Potenciacao(valor12, valor13):
    print("O total da conta desejada é:", valor12 ** valor13)
loop = True
while loop == True:
    conta_escolhida = int(input("""Você deseja:

1) Somar dois valores
2) Subtrair dois valores
3) Multiplicar dois valores
4) Dividir dois valores
5) Resto da divisão
6) Potenciação
7) Sair do loop

Digite o número: """))
    print("")
    if conta_escolhida == 1:
        Soma(int(input("Qual o primeiro valor? ")), int(input("Qual o segundo valor? ")))
    elif conta_escolhida == 2:
        Subtracao(int(input("Qual o primeiro valor? ")), int(input("Qual o segundo valor? ")))
    elif conta_escolhida == 3:
        Multiplicacao(int(input("Qual o primeiro valor? ")), int(input("Qual o segundo valor? ")))
    elif conta_escolhida == 4:
        Divisao(int(input("Qual o primeiro valor? ")), int(input("Qual o segundo valor? ")))
    elif conta_escolhida == 5:
        Resto(int(input("Qual o primeiro valor? ")), int(input("Qual o segundo valor? ")))
    elif conta_escolhida == 6:
        Potenciacao(int(input("Qual o primeiro valor? ")), int(input("Qual o segundo valor? ")))
    elif conta_escolhida == 7:
        loop = False