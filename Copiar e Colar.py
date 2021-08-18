vezes = int(input("Quantas vezes deseja que seu texto seja escrito? "))
vez_atual = 1
texto = input("O quê você deseja que seja escrito? ")
while vez_atual <= vezes:
    print(texto)
    vez_atual += 1
print("Prontinho! Texto escrito!")