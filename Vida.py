life=100
armor=50
damagetaken=int(input("Voc� deseja atacar um inimigo com quanto de ataque? (Somente n�meros!)"))
immunetodamage=input("Voc� vai ser invenc�vel? (Somente sim ou n�o!)")
if (damagetaken<=armor):
    print("Voc� n�o recebeu dano.")
elif (damagetaken>armor) and (immunetodamage=="N�o"):
    print("Sua vida atual �:", life-(damagetaken-armor))
else:
    print("Voc� n�o recebeu dano.")