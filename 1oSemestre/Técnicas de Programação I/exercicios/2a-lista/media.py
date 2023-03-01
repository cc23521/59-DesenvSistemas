from decimal import Decimal, getcontext

# Limita as notas a apenas uma casa decimal
getcontext().prec = 2

# Armazena a sequência de notas para cada disciplina
geografia = []
matematica = []
portugues = []

# Inputa as notas para Geografia, Matemática e Português, respectivamente
while True:
    if len(geografia) < 3:
        print(f"{len(geografia)} notas para Geografia inseridas")
        geografia.append(Decimal(input("Insira a nota para Geografia: ")))
    elif len(matematica) < 3:
        print(f"{len(matematica)} notas para Matemática inseridas")
        matematica.append(Decimal(input("Insira a nota para Matemática: ")))
    elif len(portugues) < 3:
        print(f"{len(portugues)} notas para Português inseridas")
        portugues.append(Decimal(input("Insira a nota para Português: ")))
    else:
        break

notaGeografia = sum(geografia) / 3
notaMatematica = sum(matematica) / 3
notaPortugues = sum(portugues) / 3
mediaExercicios = (notaGeografia + notaMatematica + notaPortugues) / 3
aproveitamento = ((notaGeografia + notaMatematica * 2 + notaPortugues * 3) + mediaExercicios) / 7

print("Média de aproveitamento é {aproveitamento}")
print("Conceito do aluno é ", end="")
if aproveitamento >= 9.0:
    print("A")
elif (aproveitamento >= 7.5) and (aproveitamento < 9.0):
    print("B")
elif (aproveitamento >= 6.0) and (aproveitamento < 7.5):
    print("C")
else:
    print("D")

