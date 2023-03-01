idade = int(input("Insira a idade do atleta: "))

infantil_A = range(5,8)
infantil_B = range(8,11)
infanto_juvenil = range(11,14)
juvenil = range(14,17)
junior = range(17,21)

if idade in infantil_A:
    print("Infantil A")
elif idade in infantil_B:
    print("Infantil B")
elif idade in infanto_juvenil:
    print("Infanto-Juvenil")
elif idade in juvenil:
    print("Juvenil")
elif idade in junior:
    print("Junior")
elif idade > 20:
    print("Adulto")
else:
    print("Idade inválida")
