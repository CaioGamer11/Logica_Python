Nota= int(input("Qual foi sua nota de 1 á 4?"))
if Nota == 1:
    print("Sua nota foi muito baixa.")
elif Nota == 2:
    print("Sua nota não foi tão ruim, mas não atingiu a média.")
elif Nota == 3:
    print("Sua nota atingiu a média.")
elif Nota == 4:
    print("Parabéns! Sua nota foi máxima!")
else:
    print("Esta nota não é válida.")