life=100
armor=50
damagetaken=int(input("Você deseja atacar um inimigo com quanto de ataque? (Somente números!)"))
immunetodamage=input("Você vai ser invencível? (Somente sim ou não!)")
if (damagetaken<=armor):
    print("Você não recebeu dano.")
elif (damagetaken>armor) and (immunetodamage=="Não"):
    print("Sua vida atual é:", life-(damagetaken-armor))
else:
    print("Você não recebeu dano.")