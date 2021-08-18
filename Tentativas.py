tentativas = 3
correto = False
while (tentativas>0) and not (correto):
    user = input("Qual é meu nome? ")
    if user=="Caio":
        print('Parabéns, você acertou!')
        correto = True
    else:
        tentativas -= 1
        print("Você errou, suas tentativas restantes são:", tentativas)