def mostraResultado():
    print(f"Pessoas consultadas: {pessoas}")
    print(f"Pessoas maiores de idade: {maiores}")
    print(f"Pessoas menores de idade: {menores}")
    print(f"Pessoas com 18 anos: {com18}")

menores = 0
maiores = 0
maioresHomens = 0
pessoas = 0
while True:
    idade = int(input("Quantos anos você tem? (<0 para terminar execução) "))
    if (idade <= 0):
        print("Idade inválida")
        break
    else:
        sexo = input("Qual o seu sexo? [M/F] ")
        sexo = sexo[0].upper()
        if (idade < 18):
            menores += 1
        elif (idade > 18):
            maiores += 1
            if (sexo == 'M'):
                maioresHomens += 1
    pessoas += 1
com18 = pessoas - (menores + maiores)
mostraResultado()

