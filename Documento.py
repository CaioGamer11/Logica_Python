Documento= input("Com qual documento você vai se registar?")
if Documento == "CPF":
    print("Você vai se registrar com seu CPF.")
elif Documento == "RG":
    print("Você vai se registrar com seu RG.")
elif Documento == "CNH":
    print("Você vai se registrar com seu CNH.")
else:
    print("Este não é um documento válido.")