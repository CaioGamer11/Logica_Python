a = [1, 2, 3, 4, 5]
for b in a:
    print(b*2)
c = ["Alice", "Bianca", "Carol", "Denise", "Elena"]
d = input("Qual nome você deseja trocar? Alice, Bianca,\nCarol, Denise ou Elena? ")
e = c.index(d)
c[e] = input("Digite o novo nome, por favor: ")
print("A nova lista de nomes é:", c)
f = []

h = int(input("Quantos avisos você deseja cadastrar? "))
i = 1
while (i <= h):
    f.append(input("Digite sua mensagem: "))
    i += 1
for g in f:
    print(g)
j = 1
k = ["Alice", "Bianca", "Carol", "Denise", "Elena"]
for l in k:
    print("O", j, "º nome cadastrado foi:", l)
    j += 1