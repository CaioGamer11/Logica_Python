tentativas = 3
correto = False
while (tentativas>0) and not (correto):
    user = input("Qual � meu nome? ")
    if user=="Caio":
        print('Parab�ns, voc� acertou!')
        correto = True
    else:
        tentativas -= 1
        print("Voc� errou, suas tentativas restantes s�o:", tentativas)