Islife= True
life= 100
armor=50
damagetaken= int(input("Deseja enfrentar um inimigo de quanto dano? (Somente n�meros!)"))
life = life-(damagetaken-armor)
if (Islife== False) or (life<=0):
    print("Voc� perdeu o jogo!")