geo = float(input("Insira a nota para Geografia: "))
port = float(input("Insira a nota para Português: "))
mat = float(input("Insira a nota para Matemática: "))

media = (geo + port + mat) / 3
aproveitamento = round(((geo + port * 2 + mat * 3) + media) / 7, 1)

print(f"\nMédia de aproveitamento é {aproveitamento}")
print("Conceito do aluno é ", end="")
if aproveitamento >= 9.0:
    print("A")
elif (aproveitamento >= 7.5) and (aproveitamento < 9.0):
    print("B")
elif (aproveitamento >= 6.0) and (aproveitamento < 7.5):
    print("C")
else:
    print("D")

